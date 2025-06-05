<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Collaborative Code Editor</title>
  <style>
    body { margin: 0; font-family: Arial, sans-serif; background: #282c34; color: white; }
    #editor { height: 90vh; width: 100%; }
    #status { padding: 10px; background: #20232a; text-align: center; font-size: 0.9em; }
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.23.4/ace.js" integrity="sha512-WP2KjeAr4OHZaYymub9HgKYo9FPA4+xyvDCVZJUVsmy8RihDPGsh3Et4o4NcLhB9V1mRAaqV3rpjA1JKCdHPhQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://cdn.socket.io/4.7.2/socket.io.min.js" integrity="sha384-9O5jzGBAtvlz70z5q9+rJK9HgpnJV4o7RZmqKqGJ5zYwYOKodMKME+OBVYQ+ABdH" crossorigin="anonymous"></script>
</head>
<body>
  <div id="editor">// Start coding...</div>
  <div id="status">Connecting to server...</div>

  <script>
    const editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/javascript");
    editor.setOptions({ fontSize: "14pt", showPrintMargin: false });

    const socket = io("http://localhost:3000");

    socket.on("connect", () => {
      document.getElementById("status").textContent = "Connected as " + socket.id;
    });

    editor.session.on("change", delta => {
      if (!editor.ignoreNextChange) {
        socket.emit("code_change", delta);
      }
    });

    socket.on("code_change", delta => {
      editor.ignoreNextChange = true;
      editor.session.getDocument().applyDeltas([delta]);
      editor.ignoreNextChange = false;
    });
  </script>
</body>
</html>
