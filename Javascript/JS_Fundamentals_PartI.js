var x = [3,5,'Dojo', 'rocks', 'Michael', 'Sensei'];
x.push(100);
new_array =  ["hello", "world", "JavaScript is Fun"];
x.push(new_array);
for (var i = 0; i < x.length; i++) {
console.log(x[i]);
}

var sum=0;
for (var n=0; n<501; n++) {
  sum=sum + n;
}
console.log(sum);

var arr =  [1, 5, 90, 25, -3, 0];
var min = 0;
for (var y=0; y<arr.length; y++) {
    if (arr[y] < min) {
        min = arr[y];
    }
}
console.log (min);

var array =  [1, 5, 90, 25, -3, 0];
var sum = 0;
var avg = 0;
for (var i=0; i<array.length; i++) {
    sum = sum + array[i];
    avg = sum/array.length;
}
console.log (avg);

var new_ninja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}
for(var key in new_ninja) {
    console.log(key, new_ninja[key]);
}
//console.log(new_ninja.name, new_ninja.profession, new_ninja.favorite_language, new_ninja.dojo);
