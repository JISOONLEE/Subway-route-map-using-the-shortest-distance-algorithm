<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
<style>
</style>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Insert title here</title>
</head>
<body>
    <div style="margin:30px">
    	
    	<h1>지하철 노선도</h1> 
    	<p>
    	<ul class="list-group" style="width:700px">
    		<li class="list-group-item">${start}  ->  ${finish}</li>
  			<li class="list-group-item">개발자: ${developer} / 알고리즘: ${algorithm}</li>
  			<li class="list-group-item">경로: ${route}</li>
  			<li class="list-group-item">환승: ${transfer}</li>
			<li class="list-group-item">이동거리(m): ${distance}</li>
		</ul>
    </div>
</body>
</html>