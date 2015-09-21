function longestLines(numberOfLinesToCheckLongest, lines){
    var self = this;
    var numberOfLines = numberOfLinesToCheckLongest;
    var lines = lines;

    //Sort the beast
    lines.sort(function(a, b){
        return b.length - a.length;
    });

    self.GetLinesAndPrint = function(){
        var result = lines.slice(0, numberOfLines);
        self.PrintLines(result);
        return result;
    }

    self.PrintLines = function(specificLines){
        debugger;
        var linesToPrint = lines;
        if("object" == typeof(specificLines)){
            linesToPrint = specificLines;
        }

        linesToPrint.forEach(function(line){
            console.log(line);
        });
    }

    return self;
}

if (require.main == module){
    var fs  = require("fs");
    var numOfLines = 0;
    var lines = [];
    var counter = 0;
    
    fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
        if (line != "") {
            if(counter == 0 && !isNaN(Number(line))){
                numOfLines = Number(line);
            } else if ("string" == typeof(line)){
                lines.push(line);
            }
        }
    });

    var object = new longestLines(numOfLines, lines);
    object.GetLinesAndPrint();         
}


