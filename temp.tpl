<!DOCTYPE html>
<html>
  <head>
    <title>test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script type="text/javascript" src="/static/js/scriptjava.js"></script>
    <script src="/static/js/jquery.min.js"></script> 
    <script type="text/javascript" src="/static/js/my.js"></script>
  </head>
  <body>	
    <div class ="container">
	%submitdis=""
        %roledis=""
        %deldis=""
	%if role==0:
	%vivod=name + " - superuser"	
      <h1>
	{{vivod}}
     </h1>
	<table border=0>
	<tr>
        <td><input id="name" type="text" name="name" placeholder="username"></td>
        <td><input id="passwd" type="password" name="passwd" placeholder="password"></td>
        <td><select id="role" name="role">
          <option>0</option>
          <option>1</option>
	  <option>2</option>
        </select></td>
        <td><button onclick="SendCheckUsername();">add</button></td>
	</tr>
	</form>
	</table>
	%end
	
	%if role==1:
	%vivod=name + " - user"
	%roledis="disabled"
	%deldis="disabled"
	<h1>{{vivod}}</h1>
	%end
	
	%if role==2:
        %vivod=name + " - guest"
	%roledis="disabled"
	%deldis="disabled"
        <h1>{{vivod}}</h1>
        %end

	<br><br>
	<table border=0>
	<tr><td>username</td><td>password</td><td>role</td></tr>
	%for list in all:
	%user = list['name']
	%passwd = list['pass']
	%role = list['role']
	%sellist = [0,1,2]
	%sellist.remove(role)
	<tr>
	<form action="/change_user" method="POST">
        <td><input type="text" name="name" readonly value={{user}}></td>
        <td><input type="password" name="passwd"></td>
	<td><select name="role">
	  <option>{{role}}</option>
	  <option {{roledis}}>{{sellist[0]}}</option>
	  <option {{roledis}}>{{sellist[1]}}</option>
	</select></td>
        <td><input type="submit" value="change" {{submitdis}}/></td>
        </form>
	<form action="/delete_user" method="POST">
	<td><input type="hidden" name="namedel" value={{user}}></td>
	<td><input type="submit" value="remove" {{deldis}}/></td>
	</form>
	</tr>
	%end
	</table>
    </div>

  </body>
</html>
