$(document).ready(function(){
    $('#adduserform').hide()
    $('#newuser').on("click",function(){
        $('#username').removeAttr('readonly')
        $('#adduserform').show()
        $('#usertable').hide()
        $('#newuser').hide()

    })
    $('#canceluser').on("click",function(){
        $('#adduserform').hide()
        $('#usertable').show()
        $('#newuser').show()

    })
    $('a[name="edituser"]').on("click",function(){
       $.ajax({
        url: 'edituser',
        data: {
          'userid': $(this).parent().parent().attr('id')
        },
        success: function (data) {
            $('#adduserform').show()
            $('#usertable').hide()
            $('#newuser').hide()
            $('#username').prop('readonly','true')
            $('#username').val(data['username'])
            $('#email').val(data['email'])
            $('#usertype').val(data['groups__name'])
        }
      });
    })
});