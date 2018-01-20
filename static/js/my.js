function SendCheckUsername() {
	var alldata;
	name=document.getElementById("name").value;
	passwd=document.getElementById("passwd").value;
	role=document.getElementById("role").value;
        $$a({
		async: false,
                type:'post',
                url:'/create_user_by_ajax',
                data:{'name':name,'passwd':passwd,'role':role},
                response:'text',
		success: function(response) {
			alldata=response
            }
        });
	alert(alldata)
	if(alldata == "user is created") document.location.href = "/";
}
