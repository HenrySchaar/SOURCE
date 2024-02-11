let os = require("os");
let r1 = os.freemem() / (1000*1000*1000);
let r2 = os.freemem() / (1024*1024*1024);


console.log("Free memory: ", r1, " Gigabyte" )
let r3 = input()