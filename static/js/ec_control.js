function gettime() {
    $.ajax({
        url: "/time",
        timeout: 10000,
        success: function (data) {
            $("#time").html(data)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function getc1data() {
    $.ajax({
        url: "/c1",
        timeout: 10000,
        success: function (data) {
            $(".num h1").eq(0).text(data.confirm)
            $(".num h1").eq(1).text(data.suspect)
            $(".num h1").eq(2).text(data.heal)
            $(".num h1").eq(3).text(data.dead)

        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function getc2data() {
    $.ajax({
        url: "/c2",
        timeout: 10000,
        success: function (data) {
            ec_center_option.series[0].data = data.data
            ec_center.setOption(ec_center_option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function getl1data() {
    $.ajax({
        url: "/l1",
        timeout: 10000,
        success: function (data) {
                ec_left1_Option.xAxis[0].data = data.day,
                ec_left1_Option.series[0].data = data.confirm,
                ec_left1_Option.series[1].data = data.suspect,
                ec_left1_Option.series[2].data = data.heal,
                ec_left1_Option.series[3].data = data.dead
                ec_left1.setOption(ec_left1_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function getl2data() {
    $.ajax({
        url: "/l2",
        timeout: 10000,
        success: function (data) {
                ec_left2_Option.xAxis[0].data = data.day,
                ec_left2_Option.series[0].data = data.confirm_add,
                ec_left2_Option.series[1].data = data.suspect_add,
                ec_left2.setOption(ec_left2_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function getr1data() {
    $.ajax({
        url: "/r1",
        timeout: 10000,
        success: function (data) {
                ec_right1_option.xAxis.data = data.city,
                ec_right1_option.series[0].data = data.confirm,
                ec_right1.setOption(ec_right1_option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function getr2data() {
    $.ajax({
        url: "/r2",
        timeout: 10000,
        success: function (data) {
                ec_right2_option.series[0].data = data.kws,
                ec_right2.setOption(ec_right2_option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}



getc1data()
gettime()
getc2data()
getl1data()
getl2data()
getr1data()
getr2data()
setInterval(getc1data, 1000)
setInterval(gettime, 10000)
setInterval(getc2data, 10000)
setInterval(getl1data, 10000)
setInterval(getl2data, 10000)
setInterval(getr1data, 10000)
setInterval(getr2data, 10000)