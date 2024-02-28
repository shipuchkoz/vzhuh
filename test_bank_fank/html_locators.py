from config.setting_bank import *
from config.action import *
from bs4 import BeautifulSoup

def generate_select_locator(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    select_elements = soup.find_all('select', {'ng-model': 'custId'})
    locators = []
    for select in select_elements:
        locators.append(f"//select[@ng-model='custId']")
    return locators

html_content = """<html><head><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>

	<title>XYZ Bank</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>

<body ng-app="BankApp" ng-controller="bodyCtrl" style="background:#e8e8e8;" class="ng-scope">
	<!-- uiView:  --><div ui-view="" class="ng-scope"><div class="container-fluid ng-scope">
	<div class="box mainhdr">
		<button class="btn home" ng-click="home()">Home</button>
		<strong class="mainHeading">XYZ Bank</strong>
		<button ng-show="logout" class="btn logout ng-hide" ng-click="byebye()">Logout</button>
		
	</div>
	<!-- uiView:  --><div ui-view="" class="ng-scope"><div class="borderM box padT20 ng-scope">

<form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
</div></div>

</div></div>

	<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.7/angular.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.15/angular-ui-router.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	
	<script type="text/javascript" src="app.js"></script>
	<script type="text/javascript" src="user.service.js"></script>
	<script type="text/javascript" src="account.service.js"></script>
	<script type="text/javascript" src="transaction.service.js"></script>
	<script type="text/javascript" src="mockDataLoadService.js"></script>
	<script type="text/javascript" src="customer.data.js"></script>
	<script type="text/javascript" src="config.js"></script>
	<script type="text/javascript" src="date.search.filter.js"></script>
	<script type="text/javascript" src="accountViewController.js"></script>
	<script type="text/javascript" src="addCustomerController.js"></script>
	<script type="text/javascript" src="customerViewController.js"></script>
	<script type="text/javascript" src="bodyController.js"></script>
	<script type="text/javascript" src="depositController.js"></script>
	<script type="text/javascript" src="listCustomerController.js"></script>
	<script type="text/javascript" src="mainController.js"></script>
	<script type="text/javascript" src="managerViewController.js"></script>
	<script type="text/javascript" src="openAccountController.js"></script>
	<script type="text/javascript" src="optionsController.js"></script>
	<script type="text/javascript" src="transactionSummaryController.js"></script>
	<script type="text/javascript" src="withdrawlController.js"></script>



    </body></html>
Outer HTML for element: <head><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>

	<title>XYZ Bank</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
Outer HTML for element: <style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>
Outer HTML for element: <title>XYZ Bank</title>
Outer HTML for element: <link rel="stylesheet" type="text/css" href="style.css">
Outer HTML for element: <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
Outer HTML for element: <body ng-app="BankApp" ng-controller="bodyCtrl" style="background:#e8e8e8;" class="ng-scope">
	<!-- uiView:  --><div ui-view="" class="ng-scope"><div class="container-fluid ng-scope">
	<div class="box mainhdr">
		<button class="btn home" ng-click="home()">Home</button>
		<strong class="mainHeading">XYZ Bank</strong>
		<button ng-show="logout" class="btn logout ng-hide" ng-click="byebye()">Logout</button>
		
	</div>
	<!-- uiView:  --><div ui-view="" class="ng-scope"><div class="borderM box padT20 ng-scope">

<form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
</div></div>

</div></div>

	<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.7/angular.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.15/angular-ui-router.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	
	<script type="text/javascript" src="app.js"></script>
	<script type="text/javascript" src="user.service.js"></script>
	<script type="text/javascript" src="account.service.js"></script>
	<script type="text/javascript" src="transaction.service.js"></script>
	<script type="text/javascript" src="mockDataLoadService.js"></script>
	<script type="text/javascript" src="customer.data.js"></script>
	<script type="text/javascript" src="config.js"></script>
	<script type="text/javascript" src="date.search.filter.js"></script>
	<script type="text/javascript" src="accountViewController.js"></script>
	<script type="text/javascript" src="addCustomerController.js"></script>
	<script type="text/javascript" src="customerViewController.js"></script>
	<script type="text/javascript" src="bodyController.js"></script>
	<script type="text/javascript" src="depositController.js"></script>
	<script type="text/javascript" src="listCustomerController.js"></script>
	<script type="text/javascript" src="mainController.js"></script>
	<script type="text/javascript" src="managerViewController.js"></script>
	<script type="text/javascript" src="openAccountController.js"></script>
	<script type="text/javascript" src="optionsController.js"></script>
	<script type="text/javascript" src="transactionSummaryController.js"></script>
	<script type="text/javascript" src="withdrawlController.js"></script>



    </body>
Outer HTML for element: <div ui-view="" class="ng-scope"><div class="container-fluid ng-scope">
	<div class="box mainhdr">
		<button class="btn home" ng-click="home()">Home</button>
		<strong class="mainHeading">XYZ Bank</strong>
		<button ng-show="logout" class="btn logout ng-hide" ng-click="byebye()">Logout</button>
		
	</div>
	<!-- uiView:  --><div ui-view="" class="ng-scope"><div class="borderM box padT20 ng-scope">

<form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
</div></div>

</div></div>
Outer HTML for element: <div class="container-fluid ng-scope">
	<div class="box mainhdr">
		<button class="btn home" ng-click="home()">Home</button>
		<strong class="mainHeading">XYZ Bank</strong>
		<button ng-show="logout" class="btn logout ng-hide" ng-click="byebye()">Logout</button>
		
	</div>
	<!-- uiView:  --><div ui-view="" class="ng-scope"><div class="borderM box padT20 ng-scope">

<form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
</div></div>

</div>
Outer HTML for element: <div class="box mainhdr">
		<button class="btn home" ng-click="home()">Home</button>
		<strong class="mainHeading">XYZ Bank</strong>
		<button ng-show="logout" class="btn logout ng-hide" ng-click="byebye()">Logout</button>
		
	</div>
Outer HTML for element: <button class="btn home" ng-click="home()">Home</button>
Outer HTML for element: <strong class="mainHeading">XYZ Bank</strong>
Outer HTML for element: <button ng-show="logout" class="btn logout ng-hide" ng-click="byebye()">Logout</button>
Outer HTML for element: <div ui-view="" class="ng-scope"><div class="borderM box padT20 ng-scope">

<form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
</div></div>
Outer HTML for element: <div class="borderM box padT20 ng-scope">

<form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
</div>
Outer HTML for element: <form role="form" name="myForm" ng-submit="showAccount()" class="ng-pristine ng-valid">
	<div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
    <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
  </form>
Outer HTML for element: <div class="form-group"><label>Your Name :</label>
		<select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
	</div>
Outer HTML for element: <label>Your Name :</label>
Outer HTML for element: <select class="form-control ng-pristine ng-untouched ng-valid" name="userSelect" id="userSelect" ng-model="custId">
	      <option value="">---Your Name---</option> <!-- not selected / blank option -->
	      <!-- ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option><!-- end ngRepeat: cust in Customers --><option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option><!-- end ngRepeat: cust in Customers -->
	    </select>
Outer HTML for element: <option value="">---Your Name---</option>
Outer HTML for element: <option ng-repeat="cust in Customers" value="1" class="ng-binding ng-scope">Hermoine Granger</option>
Outer HTML for element: <option ng-repeat="cust in Customers" value="2" class="ng-binding ng-scope">Harry Potter</option>
Outer HTML for element: <option ng-repeat="cust in Customers" value="3" class="ng-binding ng-scope">Ron Weasly</option>
Outer HTML for element: <option ng-repeat="cust in Customers" value="4" class="ng-binding ng-scope">Albus Dumbledore</option>
Outer HTML for element: <option ng-repeat="cust in Customers" value="5" class="ng-binding ng-scope">Neville Longbottom</option>
Outer HTML for element: <button class="btn btn-default ng-hide" type="submit" ng-show="custId != ''">Login</button>
Outer HTML for element: <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.7/angular.min.js"></script>
Outer HTML for element: <script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.15/angular-ui-router.min.js"></script>
Outer HTML for element: <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
Outer HTML for element: <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
Outer HTML for element: <script type="text/javascript" src="app.js"></script>
Outer HTML for element: <script type="text/javascript" src="user.service.js"></script>
Outer HTML for element: <script type="text/javascript" src="account.service.js"></script>
Outer HTML for element: <script type="text/javascript" src="transaction.service.js"></script>
Outer HTML for element: <script type="text/javascript" src="mockDataLoadService.js"></script>
Outer HTML for element: <script type="text/javascript" src="customer.data.js"></script>
Outer HTML for element: <script type="text/javascript" src="config.js"></script>
Outer HTML for element: <script type="text/javascript" src="date.search.filter.js"></script>
Outer HTML for element: <script type="text/javascript" src="accountViewController.js"></script>
Outer HTML for element: <script type="text/javascript" src="addCustomerController.js"></script>
Outer HTML for element: <script type="text/javascript" src="customerViewController.js"></script>
Outer HTML for element: <script type="text/javascript" src="bodyController.js"></script>
Outer HTML for element: <script type="text/javascript" src="depositController.js"></script>
Outer HTML for element: <script type="text/javascript" src="listCustomerController.js"></script>
Outer HTML for element: <script type="text/javascript" src="mainController.js"></script>
Outer HTML for element: <script type="text/javascript" src="managerViewController.js"></script>
Outer HTML for element: <script type="text/javascript" src="openAccountController.js"></script>
Outer HTML for element: <script type="text/javascript" src="optionsController.js"></script>
Outer HTML for element: <script type="text/javascript" src="transactionSummaryController.js"></script>
Outer HTML for element: <script type="text/javascript" src="withdrawlController.js"></script>"""
select_locators = generate_select_locator(html_content)
print(select_locators)