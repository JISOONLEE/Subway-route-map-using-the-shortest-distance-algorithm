<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
<style>
.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
}
</style>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Insert title here</title>
</head>
<body> 
    <div class="wrapper">
      <form action="Subway_route" method="post" class="row g-3 form-floating">
	    	<h1 style="text-align: center;">지하철 노선도</h1>
	    	
	    	<hr color="grey">
	    	<div class="mb-3 row">
			    <label class="col-sm-3 col-form-label">출발역</label> 
			    <div class="col-md-6"> 
				    <input type = "text" name = "start" placeholder="출발역" class="form-control">
				</div>
				<div class="col-md-2">
				    <select name = "start_line" class="form-select">
				    	<option selected>호선</option>
				    	<option value = 1>1호선</option>
				    	<option value = 2>2호선</option>
				    	<option value = 3>3호선</option>
				    	<option value = 4>4호선</option>
				    	<option value = 5>5호선</option>
				    	<option value = 6>6호선</option>
				    	<option value = 7>7호선</option>
				    	<option value = 8>8호선</option>
				    </select>
			    </div>
		    </div>
		    <div class="mb-3 row">
			    <label class="col-sm-3 col-form-label">도착역</label> 
			    <div class="col-md-6">
				    <input type = "text" name = "finish" placeholder="도착역" class="form-control">
				</div>
				<div class="col-md-2">
				    <select name = "finish_line" class="form-select">
				    	<option selected>호선</option>
				    	<option value = 1>1호선</option>
				    	<option value = 2>2호선</option>
				    	<option value = 3>3호선</option>
				    	<option value = 4>4호선</option>
				    	<option value = 5>5호선</option>
				    	<option value = 6>6호선</option>
				    	<option value = 7>7호선</option>
				    	<option value = 8>8호선</option>
				    </select>
			    </div>
		    </div>
		    <div class="mb-3 row">
			    <label class="col-sm-3 col-form-label">개발자 및 알고리즘</label> 
			    <div class="col-md-8">
				    <select name = "developer" class="form-select" class="form-control">
				    	<option selected>개발자 및 알고리즘</option>
				    	<option value="dev1_dijkstra">개발자1/다익스트라</option>
				    	<option value="dev1_floyd">개발자1/플로이드 와샬</option>
				    	<option value="dev2_dijkstra">개발자2/다익스트라</option>
				    	<option value= "dev2_spfa">개발자2/SPFA</option>
				    </select>
			    </div>
			</div>
		    
		    <hr color="grey">
		    <div class="d-grid gap-2 col-6 mx-auto">
		    	<button type="submit" class="btn btn-primary">검  색</button>
		    </div>
	    </form>
    </div>
</body>
</html>