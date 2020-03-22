var ec_left2 = echarts.init(document.getElementById('l2'), "dark")

var ec_left2_Option = {
    // 标题样式
    title: {
        text: "全国累计趋势",
        textStyle: {

        },
        left: 'left',
    },
    tooltip: {
        trigger: 'axis',
        // 指示组
        axisPointer: {
            type: 'line',
            lineStype: {
                color: '#7171C6'
            }
        }
    },
    legend: {
        data: ['累计新增确诊', '现有疑似新增'],
        left: 'right'
    },

    // 图形位置
    grid: {
        left: '4%',
        right: '6%',
        bottom: '4%',
        top: 50,
        containLabel: true
    },

    xAxis: [{
        type: 'category',
        data: []
    }],
    yAxis: [{
        type: 'value',
        axisLabel: {
            show: true,
            color: 'white',
            fontSize: 12,
            formatter: function (value) {
                if (value >= 1000) {
                    value = value / 1000 + 'k'
                }
                return value
            }
        },
        // y轴线设置显示
        axisLine: {
            show: true
        },
        // 与x轴平行的线样式
        splitLine: {
            show: true,
            lineStyle: {
                color: '#17273B',
                width: 1,
                type: 'solid',
            }
        }
    }],
    series: [
        {
            name: "新增确诊",
            type: 'line',
            smooth: true,
            data: []
        },
        {
            name: "新增疑似",
            type: 'line',
            smooth: true,
            data: []
        }]
};
ec_left2.setOption(ec_left2_Option)