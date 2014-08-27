<?php
header('Content-Type: image/jpeg');

function random_pic($dir = 'pictures')
{
	$files = glob($dir . '/*.*');
	$file = array_rand($files);
	return $files[$file]; 
}
	$outFile = random_pic();
	readfile($outFile);
?>
