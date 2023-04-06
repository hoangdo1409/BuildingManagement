function getListCompany() {
    $(this).ready(function(){
        $.ajax({
            url: CompanyList_URL,
            dataType: 'JSON',
            type: 'GET',
            success: function(data){
                var event_data = '';

                $.each(data, function(index, value){
                    event_data += '<tr>';
                    event_data += '<td scope="col">'+value.name+'</td>';
                    event_data += '<td scope="col">'+value.address+'</td>';
                    event_data += '<td scope="col">'+value.tax_code+'</td>';
                    event_data += '<td scope="col">'+value.parent_company+'</td>';
                    event_data += '<td scope="col">'+value.contact+'</td>';
                    // <a class="a" href="">Link 3</a>

                    // event_data += '<td scope="col">'+'</td>';
                    // '<button type="button" class="btn btn-danger" onclick=DeleteCompany("`+value.uuid+`")>Delete</button>
                    event_data += '<td scope="col">' 
                                    + `
                                    <div class="container mt-3">                                      
                                        <div class="dropdown">
                                            <button type="button" class="btn btn-light dropdown-toggle" data-bs-toggle="dropdown">
                                                </button>
                                        <ul class="dropdown-menu">
                                            <li><a class="dropdown-item" href="details/` + value.uuid + `/">Details</a></li>
                                            <li><a class="dropdown-item" href="" onclick=DeleteCompany("`+value.uuid+`")>Delete</a><li>
                                            <li><a class="dropdown-item" href="#">Edit</a></li>
                                        </ul>
                                        </div>
                                    </div>
                                    `
                                    +'</td>';
                    event_data += '</tr>';
                });
                $("#example").append(event_data);
                
            },
            error: function(data){
                alert("404. Please wait until the File is Loaded.");
            }
        });
    });

    $(document).ready(function(){
        $("#b_show").click(function(){
            // $("#example").toggle(1000);
            // $("#example").fadeToggle(1000);
            $("#example").slideToggle("slow");
        });
    });

}

getListCompany();

$(document).ready(function(){
    $("#b_show").click(function(){
        // $("#example").toggle(1000);
        // $("#example").fadeToggle(1000);
        $("#formCompany").slideToggle("slow");
    });
});
// function getPopUp(uuid){
//     jQuery(document.getElementById("popup")).ready(function($){
//         //open popup
//         $('.cd-popup-trigger').on('click', function(event){
//             event.preventDefault();
//             $('.cd-popup').addClass('is-visible');
//         });

//         $("#del_yes").click(function(){
//             DeleteCompany(uuid);
//         });
        
//         //close popup
//         $('.cd-popup').on('click', function(event){
//             if( $(event.target).is('.cd-popup-close') || $(event.target).is('.cd-popup') ) {
//                 event.preventDefault();
//                 $(this).removeClass('is-visible');
//             }
//         });
//         //close popup when clicking the esc keyboard button
//         $(document).keyup(function(event){
//             if(event.which=='27'){
//                 $('.cd-popup').removeClass('is-visible');
//             }
//         });
//     });
// }
// getPopUp();

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  
function getCSRFTokenValue(){
    return getCookie('csrftoken');
}

function getSessionIdValue(){
    return getCookie('sessionid');
}

function DeleteCompany(uuid){
    if (confirm("Bạn có muốn xóa không?") == true){
        $(this).ready(function(){
            $.ajaxSetup({
                headers : {
                    'CSRFToken' : getCSRFTokenValue(),
                    'X-CSRFToken' : getCSRFTokenValue(), // for --> SessionAuthentication
                },
                tryCount : 0,
                retryLimit : 3,
            });
    
            var self = this;
            var uuid_go=uuid
            if(uuid==null) {
                uuid_go=cr_uuid;
            } else {
                uuid_go=uuid;
            }
            console.log('self.uuid = ', uuid);
            $.ajax({
                url: CompanyList_URL + uuid_go + "/",
                type: "DELETE",
                async: false,
                cache: false,
                timeout: 30000,
    
                success: function (data) {
                    if(confirm)
                    toastr.success('Xóa thành công');
                    // AccountAccountGetDataTable(AccountAccountpagination["current_page"]);
                    // if(cr_uuid!=""){
                    //     $(location).prop('href', "/Account/Account/create/");
                    // }
                    // console.log(data);
                    
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    console.log(xhr.status);
                    console.log(thrownError);
                    if (xhr.textStatus == 'timeout') {
                        this.tryCount++;
                        if (this.tryCount <= this.retryLimit) {
                            //try again
                            $.ajax(this);
                            return;
                        }
                        return;
                    }
                    
                    if(is_debug){
                        $.alert({
                            title: 'Error [' + xhr.status + '] ' + thrownError ,
                            content: xhr.responseText,
                        });
                    }
                },
            });
        });
    }
    
}

function postCompanyNew(){
    $.ajaxSetup({
        headers : {
            'CSRFToken' : getCSRFTokenValue(),
            'X-CSRFToken' : getCSRFTokenValue(), // for --> SessionAuthentication
        },
        tryCount : 0,
        retryLimit : 3,
    });

    $(this).ready(function(){
        var formData = {
            "name": $("#InputNameCompany").val(),
            "address": $("#inputAddress").val(),
            "floor_count": $("#inputFloor").val(),
            "member_count": $("#inputMember").val(),
            "tax": $("#inputTax").val(),
            "parent_company": $("#inputParentCompany").val(),
            "contact": $("#inputContact").val(),
            "period": $("#inputPeriod").val(),
            "created": $("#inputCreatedBy").val(),


        };
        $.ajax({
            url: CompanyList_URL,
            type: "POST",
            async: false,
            cache: false,
            timeout: 30000,
            data: formData,
            success: function(data){
                alert('Post')
                console.log(data)
            },
            error: function(data){
                console.log(data)
                alert('noop')
            }

        });
    });
    
}


function getDataChooseParentCompany() {
        $.ajax({
            url: CompanyList_URL,
            dataType: 'JSON',
            type: 'GET',
            success: function(data){
                var event_data = '';

                $.each(data, function(index, value){
                    event_data += '<option value="' + value.uuid + '">' + value.name + '</option>'
                });
                $("#inputParentCompany").append(event_data);
                
                event_data = ''

            },
            error: function(data){
                alert("404. Please wait until the File is Loaded.");
            }
        });
}

function getDataCreatedBy() {

    $.ajaxSetup({
        headers : {
            'CSRFToken' : getCSRFTokenValue(),
            'X-CSRFToken' : getCSRFTokenValue(), // for --> SessionAuthentication
        },
        tryCount : 0,
        retryLimit : 3,
    });

    $(this).ready(function(){

        $.ajax({
            url: StaffList_URL,
            dataType: 'JSON',
            type: 'GET',
            success: function(data){
                alert("hellsfgdso")

                var event_data = '';

                $.each(data, function(index, value){
                    event_data += '<option value="' + value.username + '">' + value.username + '</option>'
                });
                $("#inputCreatedBy").append(event_data);
                
            },
            error: function(data){
                alert("404. Please wait until the File is Loaded.");
            }
        });
    });

}

function viewDetails() {
    $.ajaxSetup({
        headers : {
            'CSRFToken' : getCSRFTokenValue(),
            'X-CSRFToken' : getCSRFTokenValue(), // for --> SessionAuthentication
        },
        tryCount : 0,
        retryLimit : 3,
    });

    $(this).ready(function(){
        var formData = {
            "name": $("#InputNameCompany").val(),
            "address": $("#inputAddress").val(),
            "floor_count": $("#inputFloor").val(),
            "member_count": $("#inputMember").val(),
            "tax": $("#inputTax").val(),
            "parent_company": $("#inputParentCompany").val(),
            "contact": $("#inputContact").val(),
            "period": $("#inputPeriod").val(),
            "created": $("#inputCreatedBy").val(),
        };
    });



// getDataChooseCompany();
}
