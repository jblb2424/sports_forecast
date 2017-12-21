

var games = 'localhost:8000/api/v1/load_games_from_team/'
function httpGet(url, pk)
{
  $.ajax({
  //The URL to process the request
    'url' : url,
  //The type of request, also known as the "method" in HTML forms
  //Can be 'GET' or 'POST'
    'type' : 'GET',
  //The response from the server
    'success' : function(data) {
      if (data == "success") {
        alert('request sent!');
      }
    }
  });
}


// var data = [{
//     "For": 1,
//     "Against": 2,
// }];

function constructGraph(data)
{
var fixedData = data.map(function(d){
  return d3.entries(d);
});

var width = 300,
    height = 300,
    radius = (Math.min(width, height) / 2) / data.length;

var color = d3.scale.category10();

var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(0);
    
var labelArc = d3.svg.arc()
    .outerRadius(radius / 2)
    .innerRadius(radius / 2);

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.value; });

var svg = d3.select(".graph-panel").append("svg")
    .attr("width", width)
    .attr("height", height);

var p = svg.selectAll(".pie")
  .data(fixedData)
  .enter()
  .append("g")
  .attr("class", "pie")
  .attr("transform",function(d,i){
    return "translate(" + (width / 2) + "," + ((radius * i * 2) + radius) + ")";
  });
  
var g = p.selectAll(".arc")
  .data(function(d){
    return pie(d);
  })
  .enter().append("g")
  .attr("class", "arc");

g.append("path")
  .attr("d", arc)
  .style("fill", function(d) { return color(d.data.key); });

g.append("text")
    .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
    .text(function(d) { return d.data.key; });
}
