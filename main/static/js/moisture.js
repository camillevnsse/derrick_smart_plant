$(document).ready(function () {
  const ctx = document.getElementById("humChart").getContext("2d");

  const myChart = new Chart(ctx, {
    type: "line",
    data: {
      datasets: [{ label: "Humidité",  }],
    },
    options: {
      borderWidth: 3,
      borderColor: ['rgb(52, 158, 235)',],
    },
  });

  function addData(label, data, animation) {
    myChart.data.labels.push(label);
    myChart.data.datasets.forEach((dataset) => {
      dataset.data.push(data);
    });
    myChart.update(animation);
  }

  function removeFirstData() {
    myChart.data.labels.splice(0, 1);
    myChart.data.datasets.forEach((dataset) => {
      dataset.data.shift();
    });
  }

  const MAX_DATA_COUNT = 10;
  //connect to the socket server.
  //   var socket = io.connect("http://" + document.domain + ":" + location.port);
  var socket = io.connect();

  //receive details from server
  socket.on("updateSensorData", function (msg) {
    console.log("Received sensorData :: " + msg.date + " :: " + msg.hum_value);

    // Show only MAX_DATA_COUNT data
    if (myChart.data.labels.length >= MAX_DATA_COUNT) {
      removeFirstData();
    }
    addData(msg.date, msg.hum_value, msg.animation);
  });
});