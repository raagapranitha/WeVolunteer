<?php
$servername = "localhost";
$username = "root";
$password = "";
$conn = mysqli_connect($servername, $username, $password);
// Check connection
if ($conn -> connect_errno) {
  echo "Failed to connect to MySQL: " . $conn -> connect_error;
  exit();
}
?>

<html>
<head>

<title> Hackathon</title>
<link rel="stylesheet" href="css/style.css" type="text/css">

</head>

<body style="margin:30px">

<div id="header">
<a href="index.php" id="title"><img src="images/title.gif" alt=""></a>
<ul id="navigation">
					<li class="selected first"><a href="index.php">Home</a></li>
					<li><a href="about.php">About</a></li>
					<li><a href="menu.php">Services</a></li>
					<li><a href="contact.php">Contact Us</a></li>
				</ul>
</div>

<br>
<div class="container">

	<div id="search">

	<form method="POST">
			<legend>Search by Zipcode</legend>
			<input type="text" class="form-control" name="zipcode">
			<input type="submit" name="search" value="Search" />
	</form>
</div>

<div id="listreq">
<table>
	<?php
	#select database
$sql = "USE hackathon";
if (!mysqli_query($conn,$sql)) {
    echo "Error selecting database: " . mysqli_error($conn);
}


      
if(isset($_POST['take_req'])) { 
    
    $sql = "USE hackathon";
	if (!mysqli_query($conn,$sql)) {
	    echo "Error selecting database: " . mysqli_error($conn);
	}

	$update_sql = "UPDATE requests SET Status='Inactive' WHERE id=".$_POST['id'];
	$update_res = mysqli_query($conn,$update_sql);

	if (!$update_res) {
	    echo "Error message: ".mysqli_error($conn);
	} else { ?>
		<p style="font-size: 25px"><?php echo "Thank you for your service to ".$_POST['name']." :)"; ?></p>

		<?php
	}
    #echo $_POST['id'];
} 

if(isset($_POST['search'])) {


    //echo "Search is set";

	$list_sql = "SELECT * FROM requests where Status='Active' AND Zipcode=".$_POST['zipcode'];
	$result = mysqli_query($conn,$list_sql);

	if (!$result) {
	    echo "Error message: ".mysqli_error($conn);
	}
   

	unset($_POST['search']);

} else {
	//echo "search is not set";
	$sql = "SELECT * from requests where Status='Active'";
	$result = mysqli_query($conn,$sql);

	if (!$result) {
	    echo "Error message: ".mysqli_error($conn);
	}

}

while ($row = mysqli_fetch_array($result)) { ?>

	<tr>
		<td>
		<form method="POST">

	<fieldset style="width:500px">
	<input type="hidden" name="id" value="<?php echo $row['id']; ?>" />
	<p style="font-size: 25px">
	<b>Name:</b><input type="hidden" name="name" value="<?php echo $row['Name']; ?>" /> <?php echo $row['Name']; ?> <br>
	<b>Address:</b><input type="hidden" /> <?php echo $row['Address']; ?> <br>
	<b>Zipcode:</b><input type="hidden" /> <?php echo $row['Zipcode']; ?> <br>
	<b>Mobile:</b><input type="hidden" /> <?php echo $row['Mobile']; ?> <br>
	<b>Items:</b><input type="hidden" /> <?php echo $row['Items']; ?> <br>
</p>
	 <center><input type="submit" name="take_req" value="Take Request" style="font-size: 25px"/></center>
     </fieldset>

	  </form>
	</td>
	</tr>
    
<?php
}



#print_r($rowcount);

$conn->close();
?>

</table>

</div>

</div>

</body>
</html>
