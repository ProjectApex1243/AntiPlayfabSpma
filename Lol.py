<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My First HTML Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f0f0;
      padding: 2rem;
      text-align: center;
    }
    h1 {
      color: #333;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      background-color: #007bff;
      color: white;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Welcome to My Web Page!</h1>
  <p>This is a simple HTML page with a button.</p>
  <button onclick="alert('Hello, world!')">Click Me</button>
</body>
</html>
