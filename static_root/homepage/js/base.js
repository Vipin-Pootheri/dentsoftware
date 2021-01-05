$(document).ready(function(){
    $('#searchpatient').keyup(function(e){

        $.ajax({
        url: '/home/searchpatient',
        data: {
          'name': $('#searchpatient').val()
        },
        success: function (data) {

//        attach click event to dynamically added elements
            $('div[name="searcheduserprofile"]').remove()
            $.each(data,function(index,value){
                var element = $(`<div class="card border-dark ml-2 mb-1" style="width: 230px; height:120px; background-color:#a8ccd7" name="searcheduserprofile">
                    <div name="userprofcard" class="card-body " id = `+ value['id'] + `>
                        <h5 name="userprofcard" class="card-title">`+ value['firstname'] + `</h5>
                        <h6 name="userprofcard" class="card-subtitle text-muted">Ph:`+value['phonenumber']+`</h6>
                        <p  name="userprofcard"  class="card-text">`+value['location']+`</p>
                    </div>
                </div> `).on('click',function(){
                     $('#userprofile').remove()
                        $.ajax({
                            url: '/home/setpatient',
                            data: {
                              'patid': $(this).children().attr('id')
                            },
                            success: function (data) {
                                if (data['status']!='true') {
                                alert('some error occured . Please contact administrator')

                                }
                                else{
                                window.location = window.location.href
                                }
                            }
                            })
                        })//dynamically added click fuction ends here
                $('#searchprofile').append(element)
                })//for loop for search user list ends here
            }
        })
    })



})