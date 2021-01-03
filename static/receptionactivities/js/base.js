$(document).ready(function(){
       $('#addappointmentstartdate').datetimepicker({
       format: 'Y-m-d H:i',

       });
       $('#addappointmentenddate').datetimepicker({
       format: 'Y-m-d H:i',

       });
       $('#updateappointmentstartdate').datetimepicker({
       format: 'Y-m-d H:i',

       });
       $('#updateappointmentenddate').datetimepicker({
       format: 'Y-m-d H:i',

       });

//for add appointment
    $('#addappointmentpatientphonediv').hide()
    $('#newpatientappointment').change(function() {
        if(this.checked) {
            $('#addappointmentpatientphonediv').show()
        }
        else{
            $('#addappointmentpatientphonediv').hide()
        }

    })

//search for patient name in creating new appointment
    $('#addappointmentpatientname').keyup(function(){
        $.ajax({
        url: '/home/searchpatient',
        data: {
          'name': $('#addappointmentpatientname').val()
        },
        success: function (data) {

            $('div[name="addapointmnetsearchname"]').remove()
            $.each(data,function(index,value){

                element = $('<div class="form-control" name="addapointmnetsearchname" id = ' + value['id'] +'>' + '<span>' + value['firstname'] + '</span><span>'+ ' '+ value['lastname'] +  '</span><span style="float: right">Ph: '+ value['phonenumber'] + '</span> </div>').on("click",function(){
                    $('#addappointmentpatientname').val($(this).text())
                    $('#addappointmentpatientid').val($(this).attr('id'))

                })
                $('#addappointmentsearchdiv').append(element)
            })
            }
        })
    })

//update the appointment to checkin
    $('#checkin').on('click',function(){
       if ($('#checkin').text() == 'Register') {

        $('#modalupdateappointment').modal('hide')
       $.ajax({
         url: 'registerafterappointment',
         data: {
          'id': $('#updateappointmentid').val()
        },
        success: function (data) {
            window.location.href=data['url']+'/reception/newpatient/'
        }
        })

       }else{
         $.ajax({
         url: 'checkin',
         data: {
          'id': $('#updateappointmentid').val()
        },
        success: function (data) {
            if(data['status'] == 'true'){
            alert("User checked in sucessfully")
             $('#modalupdateappointment').modal('hide')
             location.reload()

            }
            else{
            alert('error occured')
            }
            }
        })
        }
    })

//update the appointment
    $('#updateappointment').on('click',function(){
        $.ajax({
         url: 'update',
         data: {
          'id': $('#updateappointmentid').val(),
          'start':$('#updateappointmentstartdate').val(),
          'end':$('#updateappointmentenddate').val(),
          'doctor':$('#updateappointmentdoctor').val(),
        },
        success: function (data) {
        $('#modalupdateappointment').modal('hide')
             location.reload(true)
        }
        })
    })

//delete the appointment

    $('#deleteappointment').on('click',function(){

        $.ajax({
         url: 'delete',
         data: {
          'id': $('#updateappointmentid').val()
            },
         success: function (data) {
            if(data['status'] == 'true'){
                alert("Appointment deleted sucessfully")
                $('#modalupdateappointment').modal('hide')
                window.location = window.location.href;
            }
            else{
            alert('error occured')
            }
            }
         })
    })




//populate state on country change

    $('#country').on('change',function(){
        $.ajax({
         url: 'getstate/',
         data: {
           country:$('#country').val()
         },
          success: function (data) {
                if (data['status']=='true'){
                    $.each(data['states'],function(index,value){
                        $('#state').append(
                        '<option value='+value['id'] +'>'+ value['name'] +'</option>'
                        )
                    })
                }
                else{
                    alert("error in getting state list. Error message: "+ data['errmsg'] )
                }
          }

        })
    })
//create new patient
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

    $('#patientsubmit').on('click',function(){

        var status=0
        if ($('#firstname').val() == ''){
            alert('Please fill first name field')
            status=1
        }
        if ($('#lastname').val() == ''){
            alert('Please fill last name field')
            status=1
        }
        if ($('input[type="radio"]:checked').length ==0){
            alert('Please select gender field')
            status=1
        }
        if ($('#phonenumber').val() == ''){
            alert('Please fill phonenumber')
            status=1
        }
        if ($('#addressline1').val() == ''){
            alert('Please fill addressline1')
            status=1
        }
        if ($('#location').val() == ''){
            alert('Please fill location')
            status=1
        }
        if (status == 0) {
        $.ajaxSetup({
             beforeSend: function(xhr, settings) {
             if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('#csrf_token').val());
                }
             }
        });
        $.ajax({
         url: 'createnewpatient/',
         method:'POST',
         data: {
             salutation: $('#salutation').val(),
             firstname: $('#firstname').val(),
             middlename: $('#middlename').val(),
             lastname: $('#lastname').val(),
             year: $('#id_dob_year').val() ,
             month:$('#id_dob_month').val() ,
             day: $('#id_dob_day').val() ,
             gender: $('input[type="radio"]:checked').val(),
             phonenumber: $('#phonenumber').val() ,
             email: $('#email').val(),
             addressline1: $('#addressline1').val(),
             addressline2: $('#addressline2').val(),
             addressline3: $('#addressline3').val(),
             location: $('#location').val(),
             country: $('#country').val(),
             postcode: $('#postcode').val(),
             state: $('#state').val(),
             city: $('#city').val()
         },
        success: function (data) {
                if (data['status'] == 'true') {
                    $('#regno').text(data['patid'])
                    $('#modalconfirmcheckin').modal('show');
                }
                else{
                alert('Unexpected error occured. Please contact Administrator by giving the following error message.' + data['errmsg'])
                }
            }

        })
        }
    })


    $('#confirmcheckin').on('click',function(){
        $.ajax({
         url: '/home/setpatient/',
         data: {
            patid:   $('#regno').val()
            },
         success: function (data) {
              $('#modalconfirmcheckin').modal('hide');
              $('#modalcheckin').modal('show');

         }
         })

    })

//side panel checkin

    $('#sidepanelcheckin').on("click",function(){
        if ($('div[name="userprofcard"]').length){
              $('#modalcheckin').modal('show')
        }
        else{
            alert('plese select a patiemt to check in')
        }
    })
    $('#checkinerror').on("click",function(){
        alert("You are not authorised to perform this action")
    })

    $('#checkinwalkin').on("click",function(){
        $.ajax({
         url: '/home/checkinwalkin/',
         data: {
          'patid': $('div[name="userprofcard"]').attr('id'),
          'doctorid': $('#checkindoctor').val()
        },
        success: function (data) {
            if(data['status'] == 'true'){
            alert("User checked in sucessfully")
             $('#modalcheckin').modal('hide')
             location.reload('/')

            }
            else{
            alert('error occured')
            }
            }
        })

    })

})