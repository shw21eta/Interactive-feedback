var densityCanvas = document.getElementById("densityChart");

  Chart.defaults.global.defaultFontFamily = "Lato";
  Chart.defaults.global.defaultFontSize = 18;

  var densityData = {
    label: 'Positive Responses',
    data: {{positive}},
    backgroundColor: 'rgba(0, 99, 132, 0.6)',
    borderWidth: 0,
    yAxisID: "y-axis-density"
  };

  var gravityData = {
    label: 'Negative Responses',
    data: {{negative}},
    backgroundColor: 'rgba(99, 132, 0, 0.6)',
    borderWidth: 0,
    yAxisID: "y-axis-gravity"
  };

  var planetData = {
    labels: ["CO", "Teaching style", "Intearctivity", "Understanding", "Discipline", "Exam"],
    datasets: [densityData, gravityData]
  };

  var chartOptions = {
    scales: {
      xAxes: [{
        barPercentage: 1,
        categoryPercentage: 0.6
      }],
      yAxes: [{
        id: "y-axis-density"
      }, {
        id: "y-axis-gravity"
      }]
    }
  };

  var barChart = new Chart(densityCanvas, {
    type: 'bar',
    data: planetData,
    options: chartOptions
  });

  /*
let model = {
  i: 0,
  chartMax: 0
};

let controller = {
  init: function() {
    let d = {};
    this.getData();
  },
  getData: function() {
    var myD;
    var XHR = new XMLHttpRequest();
    XHR.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        myData = JSON.parse(this.responseText);
        controller.loadChart(myData);
      }
    };
    XHR.open(
      "GET",
      "https://raw.githubusercontent.com/FreeCodeCamp/ProjectReferenceData/master/GDP-data.json"
    );
    XHR.send();
  },
  loadChart: function(obj) {
    let i = model.i;
    this.setMax(this.findMax(obj.data));

    let chartScale = d3
      .scaleLinear()
      .domain([0, model.chartMax])
      .range([0, 300]); // second # controls height

    document.getElementById("charttitle").innerHTML = `${obj.name} <small>${
      obj.description
    }</small>`;
    document.getElementById("timeline").innerHTML = `${showMonth(
      obj.from_date
    )} - ${showMonth(obj.to_date)}`;

    let barH = 100 / obj.data.length;
    d3
      .select(".chart")
      .selectAll("div")
      .data(obj.data)
      .enter()
      .append("div")
      .style("height", d => chartScale(Math.floor(d[1])) + "px")
      .style("width", barH + "%")
      // .attr("title", function(d) {
      //   return `${showMonth(d[0])} (${d[1]})`;
      // })
      .html(function(d) {
       return `<span class="tag"><strong>${getAmount(d[1])}</strong> ${showMonth(d[0])}</span>`
       })
    ;

    // this.incrementChart(); // for multi charts
  },
  findMax: function(arr) {
    let max = model.chartMax;
    let m = arr.forEach(e => {
      if (e[1] > max) {
        max = e[1];
      }
    });
    return max;
  },
  setMax: function(num) {
    model.chartMax = num;
  },
  incrementChart: function() {
    model.i++;
  }
};

controller.init();

function showMonth(timestamp) {
  let time = new Date(timestamp);
  return getMonthLabel(time.getUTCMonth()) + " " + time.getUTCFullYear();
}

function getMonthLabel(num) {
  var month = new Array();
  month[0] = "Jan";
  month[1] = "Feb";
  month[2] = "Mar";
  month[3] = "Apr";
  month[4] = "May";
  month[5] = "June";
  month[6] = "July";
  month[7] = "Aug";
  month[8] = "Sept";
  month[9] = "Oct";
  month[10] = "Nov";
  month[11] = "Dec";
  return month[num];
}
function getAmount(val) {
  return "$"+val.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,') + " billion";
}
*/
