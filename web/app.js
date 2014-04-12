void function () {
  var PORT = 12345

  var canvas = document.getElementsByTagName('canvas')[0]
  var context = canvas.getContext('2d')
  var socket = new WebSocket('ws://' + prompt('Connect to:', location.hostname + ':' + PORT))

  socket.binaryType = "arraybuffer"

  socket.onopen = function() {
    socket.onmessage = function (event) {
      var size = event.data.split('x')
      canvas.width = size[0]
      canvas.height = size[1]
      socket.onmessage = function (event) {
        var imageData = context.createImageData(canvas.width, canvas.height)
        imageData.data.set(new Uint8Array(event.data))
        context.putImageData(imageData, 0, 0)
      }
    }
  }

  socket.onclose = function() {
    confirm('Disconnected. Refresh?') && location.reload(true)
  }
} ()