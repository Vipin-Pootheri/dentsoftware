$(document).ready(function(){
//    for alerts
    $('#alertbloodpreessure').change(function() {
       if ($(this).is(':checked')){
             $("#alertbloodpreessuretext").removeAttr("disabled");
       }else{
            $("#alertbloodpreessuretext").attr("disabled", "disabled");

       }
    });
    $('#alertheartalignment').change(function() {
       if ($(this).is(':checked')){
             $("#alertheartalignmenttext").removeAttr("disabled");
       }else{
            $("#alertheartalignmenttext").attr("disabled", "disabled");

       }
    });
    $('#alertheumaticfever').change(function() {
       if ($(this).is(':checked')){
             $("#alertheumaticfevertext").removeAttr("disabled");
       }else{
            $("#alertheumaticfevertext").attr("disabled", "disabled");

       }
    });
    $('#alertasthma').change(function() {
       if ($(this).is(':checked')){
             $("#alertasthmatext").removeAttr("disabled");
       }else{
            $("#alertasthmatext").attr("disabled", "disabled");

       }
    });
    $('#alerttuberculosis').change(function() {
       if ($(this).is(':checked')){
             $("#alerttuberculosistext").removeAttr("disabled");
       }else{
            $("#alerttuberculosistext").attr("disabled", "disabled");

       }
    });
    $('#alertheart').change(function() {
       if ($(this).is(':checked')){
             $("#alerthearttext").removeAttr("disabled");
       }else{
            $("#alerthearttext").attr("disabled", "disabled");

       }
    });
    $('#alertdentalissues').change(function() {
       if ($(this).is(':checked')){
             $("#alertdentalissuestext").removeAttr("disabled");
       }else{
            $("#alertdentalissuestext").attr("disabled", "disabled");

       }
    });
    $('#alertpreviousillness').change(function() {
       if ($(this).is(':checked')){
             $("#alertpreviousillnesstext").removeAttr("disabled");
       }else{
            $("#alertpreviousillnesstext").attr("disabled", "disabled");

       }
    });
    $('#alertpresentmedicalcare').change(function() {
       if ($(this).is(':checked')){
             $("#alertpresentmedicalcaretext").removeAttr("disabled");
       }else{
            $("#alertpresentmedicalcaretext").attr("disabled", "disabled");

       }
    });
    $('#alertanydrugs').change(function() {
       if ($(this).is(':checked')){
             $("#alertanydrugstext").removeAttr("disabled");
       }else{
            $("#alertanydrugstext").attr("disabled", "disabled");

       }
    });
     $('#alertallergies').change(function() {
       if ($(this).is(':checked')){
             $("#alertallergiestext").removeAttr("disabled");
       }else{
            $("#alertallergiestext").attr("disabled", "disabled");

       }
    });
     $('#alertfemalepatients').change(function() {
       if ($(this).is(':checked')){
             $("#alertfemalepatientstext").removeAttr("disabled");
       }else{
            $("#alertfemalepatientstext").attr("disabled", "disabled");

       }
    })
//    for user authorsation
    $('#sidepanelalertsdisabled').on("click",function(){
            alert('You are not authorised to perform this action')
    })
    $('#radiologydiasbled').on("click",function(){
            alert('You are not authorised to perform this action')
    })
    $('#prescriptiondiasbled').on("click",function(){
            alert('You are not authorised to perform this action')
    })
     $('#checkoutdisabled').on("click",function(){
            alert('You are not authorised to perform this action')
    })
    $('#dentalchartdisabled').on("click",function(){
            alert('You are not authorised to perform this action')
    })


//for radiology
    $('#radiologyform').hide()
    $('#addradiology').on("click",function(){
        $('#radiologyform').show()
        $('#addradiology').hide()
        $('#radilogytable').hide()

    })
    $('#cancelradilogy').on("click",function(){
        $('#radiologyform').hide()
        $('#addradiology').show()
        $('#radilogytable').show()
    })

//    for prescription

    $('#prescriptionform').hide()
    $('#addprescription').on("click",function(){
        $('#prescriptionform').show()
        $('#addprescription').hide()
        $('#prescriptiontable').hide()
    })
    $('#cancelprescription').on('click',function(){
        $('#prescriptionform').hide()
        $('#addprescription').show()
        $('#prescriptiontable').show()
    })

//    for billing

    $('#billingform').hide()
    $('#addbilling').on('click',function(){
        $('#billingtable').hide()
        $('#addbilling').hide()
        $('#billingform').show()

    })
    $('#resetbilling').on('click',function(){
        $('#billingtable').show()
        $('#addbilling').show()
        $('#billingform').hide()
    })

//    for dental charting

    $('#addtreatmentdetail').on('click',function(){
        if ($('#diagnosislist').val()=='0'){
        alert('Please select diagnosis for selected teeth ')
        }
        else{
         $('button[name="savetreatmentplan"]').remove()
         var treatmentid = $('#treatmentdetailtable tr:last').attr('id')
         if (isNaN(treatmentid) ==true){
            treatmentid = 1
         }
         else{
            treatmentid = parseInt(treatmentid,10)+1
         }

         var starting = `<tr id=` + treatmentid + `>

            <td name="teethno">12-F</td>
            <td id=` +$('#diagnosislist').val() + ` name="diagnosis">` + $('#diagnosislist').find(":selected").text() + `</td>
            <td name="treatment"></td>
            <td name="fee"></td>
            <td name="discount"></td>
            <td name="payable"></td>
            <td name="clinicalnotes"> </td>
            <td name="doctorname">Doctor</td>
            <td name="statustreatment">Pending</td>
            <td>
                <button name="executetreatmentplan">Execute</button>
                <button name="edittreatmentplan"><i class="fa fa-edit" aria-hidden="true"></i></button>
                <button name="deletetreatmentplan"><i class="fa fa-trash" aria-hidden="true"></i></button>
             </td>
             </tr>
             `
         var tablerow = starting
        $('#treatmentdetailtablebody').append(tablerow)
        $('#treatmentdetailtable').append('<button class="mt-3" name="savetreatmentplan">Save</button>')
        }
    })

    $(document).on("click", "button[name='executetreatmentplan']" , function() {
          alert('execute')
    });
    $(document).on("click", "button[name='edittreatmentplan']" , function() {
        $('#modalid').val($(this).parent().parent().attr('id'))
        $('#modalteethno').val($(this).parent().parent().find('td:nth-child(1)').text())
        $('#modaldiagnosis').val($(this).parent().parent().find('td:nth-child(2)').attr('id'))
        $('#modaltreatement').val($(this).parent().parent().find('td:nth-child(3)').attr('id'))
        $('#modalfee').val($(this).parent().parent().find('td:nth-child(4)').text())
        $('#modaldiscount').val($(this).parent().parent().find('td:nth-child(5)').text())
        $('#modalpayable').val($(this).parent().parent().find('td:nth-child(6)').text())
        $('#modalclinicalnotes').val($(this).parent().parent().find('td:nth-child(7)').text())
        $('#modalstatus').val($(this).parent().parent().find('td:nth-child(9)').text())


        $('#modalupdatetreatment').modal('show')



    });
    $(document).on("click", "button[name='deletetreatmentplan']" , function() {
          alert('delete')
    });
     $(document).on("click", "button[name='savetreatmentplan']" , function() {
         var arr=[]
         $('#treatmentdetailtablebody tr').each(function(index,value){
            var object ={}
            object.id = $(this).attr('id')
            object.teethno = ($(this).find('td[name="teethno"]').text())
            object.diagnosis = ($(this).find('td[name="diagnosis"]').text())
            object.treatment = ($(this).find('td[name="treatment"]').text())
            object.fee = ($(this).find('td[name="fee"]').text())
            object.discount = ($(this).find('td[name="discount"]').text())
            object.payable = ($(this).find('td[name="payable"]').text())
            object.clinicalnotes = ($(this).find('td[name="clinicalnotes"]').text())
            object.doctorname = ($(this).find('td[name="doctorname"]').text())
            object.statustreatment = ($(this).find('td[name="statustreatment"]').text())

            arr.push(JSON.stringify(object))

         })

         console.log(arr[0])
          $.ajax({
             url: 'savetreatment',
             method:'POST',
             data: {
              'detail': arr
                },
             success: function (data) {
                    if(data['status']==true){
                    alert('treatment data saved sucessfully')
                    }
                }
             })
    });

//update the fee and payable based on the treatment selected

    $('#modaltreatement').on('change',function(){
          if ($('#modaltreatement').val() != '0') {
            $.ajax({
             url: 'getfee',
             method:'POST',
             data: {
              'treatmentid': $('#modaltreatement').val()
                },
             success: function (data) {
                    if(data['status']=='true'){
                        $('#modalfee').val(data['amount'])
                        $('#modaldiscount').val('0')
                        $('#modalpayable').val(data['amount'])
                    }
                     else{
                     alert('Some issue occured')
                     }
                }
             })
          }
          else{
                        $('#modalfee').val('0')
                        $('#modaldiscount').val('0')
                        $('#modalpayable').val('0')
          }
    })
    $('#modaldiscount').on('change',function(){
        fee = parseInt($('#modalfee').val())
        discount = parseInt($('#modaldiscount').val())
        payable = parseInt($('#modalpayable').val())
        if (fee>0){
            payable = fee-discount
            $('#modalpayable').val(payable)
        }
    })
    $('#modaltreatmentsave').on('click',function(){
        $.ajax({
             url: 'saveeditedtreatment',
             method:'POST',
             data: {
              'id': $('#modalid').val(),
              'teethno':$('#modalteethno').val(),
              'diagnosis':$('#modaldiagnosis').val(),
              'treatment':$('#modaltreatement').val(),
              'fee':$('#modalfee').val(),
              'discount':$('#modaldiscount').val(),
              'payable':$('#modalpayable').val(),
              'status':$('#modalstatus').val(),
              'clinicalnotes':$('#modalclinicalnotes').val(),
                },
             success: function (data) {
                $('#modalupdatetreatment').modal('hide')
                window.location = window.location.href
             }
             })
    })
})



