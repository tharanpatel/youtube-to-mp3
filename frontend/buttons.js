const exec  = require('child_process').exec;

function execute(command, callback) {
    exec(command, (error, stdout, stderr) => { 
        callback(stdout); 
    });
};

// call discord.py
function convert() {
    var url = document.getElementById('url').value;
    var pathToPyMainFile = String.raw`py PATH-TO-MAIN.PY`
    var unescapedPath = String.raw`${pathToPyMainFile} ${url}`;
    execute(unescapedPath, (output) => {
    console.log(`Executing python file using: ${unescapedPath}`);
    console.log(output)
    });
};

document.addEventListener('DOMContentLoaded', () => {
    const myButton = document.getElementById('convert');
    myButton.addEventListener('click', () => {
    convert();
    });
});

// updates yt-dlp package
function update() {
    var updateCommand = "py -m pip install -U yt-dlp";
    execute(updateCommand, (output) => {
    console.log(`Executing command: ${updateCommand}`);
    console.log(output)
    });
};

document.addEventListener('DOMContentLoaded', () => {
    const myButton = document.getElementById('update');
    myButton.addEventListener('click', () => {
    update();
    });
});