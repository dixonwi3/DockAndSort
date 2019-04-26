# may have to type Set-ExecutionPolicy Unrestricted in windows powershell, then select option "A" when prompted
# You also may have to run the script twice in order for it to pull the URL... not sure why!

docker pull openshift/base-centos7
docker run openshift/base-centos7 curl https://rgw-msu.osris.org/OsirisAdmin-keenandr/test-input | Sort-Object {[int]($_.split(":"))[3] }, {[int]($_.split(":"))[2] } > sorted-file.txt
$Dictionary = @{}
docker run openshift/base-centos7 curl https://rgw-msu.osris.org/OsirisAdmin-keenandr/test-input | foreach{($_.split(":"))[6]} |
foreach{
    $Line = $_
    If ($Dictionary.ContainsKey($Line)) {
        $Dictionary.$Line++
    } else{
        $Dictionary.Add($Line, 1)
    }
}

$Dictionary.GetEnumerator() | ?{ $_.Name.Length -lt 1000} | Sort Value -Descending >> sorted-file.txt
get-filehash C:\Users\'Will Dixon'\Desktop\scripts\sorted-file.txt 
pause