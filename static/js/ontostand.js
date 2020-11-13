// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

(function ($) {
    var methods = {
        show: function () {
            return this.each(function (i) {
                var _this = $(this);
                if (_this.css('position') !== 'absolute' && _this.css('position') !== 'relative') {
                    _this.css('position', 'relative');
                }
                   _this.prepend('<div class="myloading"><span class="fas fa-spinner fa-spin fa-2x"></span></div>');
            });
        },
        hide: function () {
            return this.each(function (i) {
                var _this = $(this);
                _this.find('.myloading').remove();
            });
        }
    };
    $.fn.myloading = function (options) {
        var method = arguments[0];
        if (methods[method]) {
            method = methods[method];
        } else if (!method) {
            method = methods.show;
        } else {
            $.error('error');
            return this;
        }
        return method.apply(this, arguments);
    }
})(jQuery);

function Process(path, id){
        $.ajax({
        url:extractorsUrl,
        type:"POST",
        data:{onto_url:path, uid:id},
        async: false,
        // error: function (data) {
        //     alert("unable to load this Ontology");
        //     },
        success:function(result){
            $('.loading-1').myloading('hide');
            $('.loading-2').myloading('hide');
            window.setTimeout(function () {
            var done = '<i class="far fa-check-circle float-right"></i>';
            console.log('ssn sensor:' + result.sensorSSN);
            console.log('sosa sensor:' + result.sensorSOSA);
            console.log('diy sensor:' + result.sensorDIY);
            console.log('sosa actuator:' + result.actuatorSOSA);
            console.log('diy actuator:' + result.actuatorDIY);
            var sensor_count= result.sensorSSN.length + result.sensorSOSA.length + result.sensorDIY.length;
            var actuator_count = result.actuatorSOSA.length + result.actuatorDIY.length;
            var $sensor_title = $("#sensor_title");
            var $sensor_div = $("#sensor_div");
            var $actuator_title = $("#actuator_title");
            var $actuator_div = $("#actuator_div");
            var $ssn_sensor_list = $("#ssn_sensor_list");
            var $ssn_sensor_count = $("#ssn_sensor_count");
            var $sosa_sensor_list = $("#sosa_sensor_list");
            var $sosa_sensor_count = $("#sosa_sensor_count");
            var $diy_sensor_list = $("#diy_sensor_list");
            var $diy_sensor_count = $("#diy_sensor_count");
            var $sosa_actuator_list = $("#sosa_actuator_list");
            var $sosa_actuator_count = $("#sosa_actuator_count");
            var $diy_actuator_list = $("#diy_actuator_list");
            var $diy_actuator_count = $("#diy_actuator_count");

            if (sensor_count === 0){
                $sensor_title.html('Sensor: None' + done);
                $sensor_div.html('There is no Sensor.');}
            else{
                $sensor_title.html('Sensor: ' + sensor_count + done );
            }
            if (actuator_count === 0){
                $actuator_title.html('Actuator: None' + done);
                $actuator_div.html('There is no Actuator.');}
            else{
                $actuator_title.html('Actuator: ' + actuator_count + done);
            }
            if (result.sensorSSN.length !== 0){
                $ssn_sensor_list.attr("style","display:block;");
                $ssn_sensor_count.html('Identified'+result.sensorSSN.length+'SSN Sensors');
                for(i = 0; i < result.sensorSSN.length; i++) {
                    var ssn_sensor_item = result.sensorSSN[i][0].toString()+ '<br/>' + result.sensorSSN[i][1].toString() ;
                    var ssn_sensor_li ="<li class=\"list-group-item\">"+ssn_sensor_item+"</li>";
                    $ssn_sensor_list.append(ssn_sensor_li);
                }}
            if (result.sensorSOSA.length !== 0){
                $sosa_sensor_list.attr("style","display:block;");
                $sosa_sensor_count.html('Identified ' + result.sensorSOSA.length + ' SOSA Sensors' + '<br/>');
                for (i = 0; i < result.sensorSOSA.length; i++) {
                    var sosa_sensor_item = result.sensorSOSA[i][0].toString() + '<br/>' + result.sensorSOSA[i][1].toString();
                    var sosa_sensor_li = "<li class=\"list-group-item\">" + sosa_sensor_item + "</li>";
                    $sosa_sensor_list.append(sosa_sensor_li);
                }}
            if (result.sensorDIY.length !== 0){
                $diy_sensor_list.attr("style","display:block;");
                $diy_sensor_count.html('Identified ' + result.sensorDIY.length + ' Self-Defined Sensors' + '<br/>');
                for(i = 0; i < result.sensorDIY.length; i++) {
                    var diy_sensor_item = result.sensorDIY[i][0].toString()+ '<br/>' + result.sensorDIY[i][1].toString() ;
                    var diy_sensor_li ="<li class=\"list-group-item\">"+diy_sensor_item+"</li>";
                    $diy_sensor_list.append(diy_sensor_li);
                }}
            if (result.actuatorSOSA.length !== 0){
                $sosa_actuator_list.attr("style","display:block;");
                $sosa_actuator_count.html('Identified ' + result.actuatorSOSA.length + ' SOSA Actuators' + '<br/>');
                for(i = 0; i < result.actuatorSOSA.length; i++) {
                    var sosa_actuator_item = result.actuatorSOSA[i][0]+ '<br/>' + result.actuatorSOSA[i][1] ;
                    var sosa_actuator_li ="<li class=\"list-group-item\">"+sosa_actuator_item+"</li>";
                    $sosa_actuator_list.append(sosa_actuator_li);
                }}
            if (result.actuatorDIY.length !== 0){
                $diy_actuator_list.attr("style","display:block;");
                $diy_actuator_count.html('Identified ' + result.actuatorDIY.length + ' Self-Defined Actuators' + '<br/>');
                for(i = 0; i < result.actuatorDIY.length; i++) {
                    var diy_actuator_item = result.actuatorDIY[i][0]+ '<br/>' + result.actuatorDIY[i][1] ;
                    var diy_actuator_li ="<li class=\"list-group-item\">"+diy_actuator_item+"</li>";
                    $diy_actuator_list.append(diy_actuator_li);
                }}
                },0)
        var load = '<i class="fas fa-cog fa-spin float-right"></i>';
        var done = '<i class="far fa-check-circle float-right"></i>';
        $.ajax({
        url:filelistUrl,
        data:{uid: id},
        type:"POST",
        success:function(filelist){
            var $rule_count = $("#rule_count");
            var $rule = $("#rule");
            $rule_count.html('Logical Rule ' + load);
            window.setTimeout(function () {
            var count = 0;
            if(filelist.length === 0){
                $rule_count.html('Logical Rule: ' + count + done);
                $("#rule_div").html('There is no Rule.');
                $.ajax({
                    url:cleanUrl,
                    type:"POST",
                    data:{uid:id},
                    success: function () {
                        console.log("Finished", id)
                    }
                })
            }else {
            for (i = 0; i < filelist.length; i++) {
                window.setTimeout(function (i) {
                    return function () {
                        $.ajax({
                            url: verbalizeUrl,
                            type: "POST",
                            data: {filename: filelist[i], uid: id},
                            async: false,
                            success: function (rule) {
                                if (rule.length !== 0) {
                                    $('.loading-3').myloading('hide');
                                    count++;
                                    $rule_count.html('Logical Rule: ' + count + load);
                                    var rule_item = rule.join(' ');
                                    var rule_li = "<li class=\"list-group-item\">" + rule_item + "</li>";
                                    $rule.append(rule_li);
                                }
                                if (i === filelist.length-1){
                                   $rule_count.html('Logical Rule: ' + count + done);
                                    if (count === 0){
                                        $("#rule_div").html('There is no Rule.');
                                    }
                                    $.ajax({
                                        url:cleanUrl,
                                        type:"POST",
                                        data:{uid:id},
                                        success: function () {
                                            console.log("Finished", id)
                                        }
                                    })
                                }
                            }
                        })
                    }
                }(i), 0)
            }
            }
            },0)
            }
        });
            }

        });
}



$(document).ready(function(){
    // select from url
    $("#btn_url").click(function(){
    var url=document.getElementById('onto_url').value;
        console.log('Ontology URL: ',url);
    if(!(url)){
        alert("Enter a valid URL or choose a local file.");
        return false
    }
    else{
        $("#input_area").attr("style","display:none;");
        $("#result-area").attr("style","display:block;");
        $('.loading-1').myloading('show');
        $('.loading-2').myloading('show');
        $('.loading-3').myloading('show');
        window.setTimeout(function () {
            var id = createUniqueId()
            Process(url, id)
        },0)
    }
    });
    // upload from file
    $("#btn_upload").click(function() {
    try {
        var f_obj = $("#upload_file").get(0).files[0];
        console.log("File Object: ", f_obj);
        console.log("File Name: ", f_obj.name);
        console.log("File Size: ", f_obj.size);
        var file_type = f_obj.name.substring(f_obj.name.lastIndexOf(".") + 1).toLowerCase();
        var file_size = f_obj.size/1024;
        var max_size = 1024*10;
        if (file_size>max_size){
            alert('File Size Maximum 10M.');
            return false
        }
        else if (file_type!=="owl" && file_type!=="rdf" && file_type!=="xml" && file_type!=="ttl" && file_type!=="n3"){
            alert('Invalid file type. Can only accept: owl rdf xml ttl n3');
            return false
        }
        else {
            $("#input_area").attr("style","display:none;");
            $("#result-area").attr("style","display:block;");
            $('.loading-1').myloading('show');
            $('.loading-2').myloading('show');
            $('.loading-3').myloading('show');
            window.setTimeout(function () {
            var data = new FormData();
            data.append("file", f_obj);
            var id = createUniqueId()
            data.append("uid", id)
            $.ajax({
                url: uploadUrl,
                type: 'POST',
                data: data,
                cache: false,
                processData: false,
                contentType: false,
                success: function (filepath) {
                    Process(filepath, id)
                }
            })
            },0)
        }
    }
    catch (e) {
        if(e instanceof TypeError){alert('Please Choose a valid file.')}
        else {alert(e)}
    }
        });


});


function createUniqueId() {
    let idStr = Date.now().toString(36)
    idStr += Math.random().toString(36).substr(3)
    return idStr
}




$(function(){
    function footerPosition(){
        $("footer").removeClass("fixed-bottom");
        var contentHeight = document.body.scrollHeight,
            winHeight = window.innerHeight;
        if(!(contentHeight > winHeight)){
            $("footer").addClass("fixed-bottom");
        } else {
            $("footer").removeClass("fixed-bottom");
        }
    }
    footerPosition();
    $(window).resize(footerPosition);
});
