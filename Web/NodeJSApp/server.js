let express = require("express");
let path = require("path");

let app = express();

app.use("/static", express.static(path.resolve(__dirname, "frontend", "static")));

app.get("/*", (req, res) =>{
    res.sendFile(path.resolve(__dirname, "frontend", "index.html")); 

});

app.listen(process.env.PORT || 8080, () => console.log("Server running!"));