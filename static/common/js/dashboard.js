/* グローバル Chart:false, feather:false */
(function () {
    'use strict'
  
    feather.replace({ 'aria-hidden': 'true' })
  
    // グラフ
    var ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    var myChart = new Chart(ctx, {
      type: 'line',
      // data: {
      //   labels: [
      //     '1月',
      //     '2月',
      //     '3月',
      //     '4月',
      //     '5月',
      //     '6月',
      //     '7月'
      //   ],
      //   datasets: [{
      //     data: [
      //       1,
      //       2,
      //       3,
      //       4,
      //       5,
      //       6,
      //       7
      //     ],
      //     lineTension: 0,
      //     backgroundColor: 'transparent',
      //     borderColor: '#007bff',
      //     borderWidth: 4,
      //     pointBackgroundColor: '#007bff'
      //   }]
      // },
      data: {
        labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        datasets: [{
          label: 'Red',
          data: [20, 35, 40, 30, 45, 35, 40],
          borderColor: '#f88',
        }, {
          label: 'Green',
          data: [20, 15, 30, 25, 30, 40, 35],
          borderColor: '#484',
        }, {
          label: 'Blue',
          data: [30, 25, 10, 5, 25, 30, 20],
          borderColor: '#48f',
        }],
      },
      options: {
        // scales: {
        //   yAxes: [{
        //     ticks: {
        //       beginAtZero: false
        //     }
        //   }]
        // },
        legend: {
          display: false
        }
      }
    })
  })()