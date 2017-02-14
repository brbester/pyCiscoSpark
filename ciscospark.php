<html>
<body>

<?php
/* Sample php script to be loaded on a web server and registered via as a webhook to the Spark API - it will receive a notification when a new message is posted and then call an external python script (sparkmess.py in this example) passing the messageid 

CAREFUL on LOOPING - make sure to only post responses to rooms in response to messages your script didn't post or you could create a loop condition and overrun your room!!!  In this example the loop prevention is in the python script, not here...
*/

$webhooksecretorig = "blalaberfasel"; # set NULL to disable check

$rawPost = NULL;
if ($webhooksecretorig !== NULL) {
	if (!isset($_SERVER['HTTP_X_SPARK_SIGNATURE'])) {
		throw new \Exception("HTTP header 'X-Spark-Signature' is missing.");
	} elseif (!extension_loaded('hash')) {
		throw new \Exception("Missing 'hash' extension to check the secret code validity.");
	}
    $hash = $_SERVER['HTTP_X_SPARK_SIGNATURE'];
	$rawPost = file_get_contents('php://input');
	if ($hash !== hash_hmac("SHA1", $rawPost, $webhooksecretorig)) {
		throw new \Exception('Hook secret does not match.');
	}
};


$json=json_decode($rawPost,true);
$txt = var_dump($json);

echo $txt;

$roomid = $json["data"]["roomId"];
echo "roomid";
echo $roomid;
$messid=$json["data"]["id"];
echo "messid";
echo $messid;

$pythonreturn = system ('python /usr/lib/cgi-bin/sparkmess.py '.$messid);
echo $pythonreturn;


/* This commented section can log to a MySQL database for tracking

$dbhost = 'localhost:3036';
$dbuser = 'root';
$dbpass = 'YOURPASSWORD';
$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}

$sql = 'INSERT INTO webhook '.
       '(JSON) '.
       'VALUES ( "'.$messid." at  ".$roomid.'")';
mysql_select_db('Ciscospark');
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
echo "Entered data successfully\n";

*/

?>

</body>
</html>

