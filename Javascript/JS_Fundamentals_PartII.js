var sum = 0;
var x=0;
var y=0;
function adding_variables(x,y){
  for (var i=x; i<(y+1); i++) {
    sum = sum + i;
  }
  console.log(sum);
}
adding_variables(1,5);


var arr = [];
var min = 0;
function findMin(arr){
for (var i=0; i<arr.length; i++) {
    if (arr[i] < min) {
        min = arr[i];
    }
  }
  console.log (min);
}
findMin([2,3,-4,6,19]);


var array = [];
var sum = 0;
var avg = 0;
function findAvg(array){
for (var i=0; i<array.length; i++) {
    sum = sum + array[i];
    avg = sum/array.length;
  }
console.log (avg);
}
findAvg([1,2,3,4,5,6,7]);


var person = {};
person = {
  name: 'Harry Potter',
  distance_traveled: 0,
}
console.log(person["name"]);


var say_something = [ function(x){console.log(person["name"]+ " " + "says" + " " + x) ;} ]

say_something[0]('I am cool');

var walk = [
  function(x, y){console.log(person["name"] + " " + x + ", " + "distance traveled is " + person.distance_traveled+y + " miles");}]

walk[0]("is walking", 3);

var run = [
  function(x, y){console.log(person["name"] + " " + x + ", " + "distance traveled is " + person.distance_traveled+y + " miles");}]
run[0]("is running", 10);

var crawl = [
  function(x, y){console.log(person["name"] + " " + x + ", " + "distance traveled is " + person.distance_traveled+y + " miles");}]
run[0]("is crawling", 1);
