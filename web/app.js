void function () {
  var PORT = 12345

  var canvas = document.getElementsByTagName('canvas')[0]
  var context = canvas.getContext('2d')
  var socket = new WebSocket('ws://' + prompt('Connect to:', location.hostname + ':' + PORT))

  socket.onopen = function() {
    socket.onmessage = function (event) {
      var size = event.data.split('x')
      canvas.width = size[0]
      canvas.height = size[1]

      function onmessage (event) {
        var image = new Image()
        image.onload = function () {
          console.log('load')
          context.drawImage(image, 0, 0)
          socket.onmessage = onmessage
        }
        image.src = "data:image/png;base64," + event.data
        delete socket.onmessage
      }
      socket.onmessage = onmessage
    }
  }

  socket.onclose = function() {
    confirm('Disconnected. Refresh?') && location.reload(true)
  }

  if ('ontouchstart' in document) {
    document.ontouchstart = function(event) {
      event.preventDefault();
    }
  }
} ()