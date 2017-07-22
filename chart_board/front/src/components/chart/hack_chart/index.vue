<template>
  <div class="comp-hack-chart">
    <div ref="chart" class="chart-wrap"></div>
  </div>
</template>

<script>
  require('./index.scss');
  const echarts = require('echarts/lib/echarts');
  require('echarts/lib/chart/line');
  require('echarts/lib/component/tooltip');
  require('echarts/lib/component/title');
  
  export default {
    props: {
      dataHack: {
        type: Array,
        default: () => {return [5, 20, 36, 10, 10, 20, 2, 10]}
      },
      dataName: {
        type: Array,
      }
    },

    mounted() {
     this.renderChart();
    },

    methods: {
      renderChart() {
        let myChart = echarts.init(this.$refs.chart);
        let option = {
          tooltip: {
            trigger: 'none',
            axisPointer: {
              type: 'cross'
            }
          },
          legend: {
            data:['表情']
          },
          grid: {
            top: 70,
            bottom: 50
          },
          xAxis: {
            type: 'category',
            axisTick: {
              alignWithLabel: true
            },
            axisLine: {
              onZero: false,
              lineStyle: {
                color: '#5793f3'
              }
            },
            axisPointer: {
              label: {
                formatter: function (params) {
                  return '表情  ' + params.value + (params.seriesData.length ? '：' + params.seriesData[0].data : '');
                }
              }
            },
            data: this.dataName,
          },

          yAxis: [{
            type: 'value'
          }],

          series: [{
            name:'表情分析',
            type:'line',
            smooth: true,
            data: this.dataHack
          }]
        };
        myChart.setOption(option);
      }
    },

    watch: {
      dataHack() {
        this.renderChart();
      }
    }
  }
</script>