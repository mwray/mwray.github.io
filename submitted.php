<style>
    h1 {color:navy;}
</style>

<?php

    $key = $_POST['key'];
    $annotations = $_POST['annotations'];

    $found = False;
    $f_name = "out" . $key . '_' . strval($num) . ".txt";

    $out_file = fopen($f_name, "w") or die("Unable to open file!");

    foreach($_POST as $k => $value) {
        if($k != "key" && $k != "num"):
            fwrite($out_file, $k." ".$value."\n");
        endif;
    }

    fclose($out_file);
?>

<div>
    <h1> Thank you for your response!</h1>

    <h2> Your Key was <?php echo $key . strval($num) ?>. </h2>
</div>

