var osx_report = executeCommand('Osxcollector', {section: args.section, system: args.system, timeout: args.timeout});
var res = [];
var maxchecks = 10;
if (args.maxchecks) {
  maxchecks = args.maxchecks;
}
for (var i=0; i<osx_report.length; i++) {
  if (osx_report[i].ContentsFormat == formats.json) {
    var content = osx_report[i].Contents;
    if (content.osxcollector_result){
      for (var j=0; j<content.osxcollector_result.length && j < maxchecks; j++) {
        if (content.osxcollector_result[j].md5) {
          var rep = executeCommand('file', {file: content.osxcollector_result[j].md5});
          if (rep && Array.isArray(rep)) {
            for (var r = 0; r < rep.length; r++) {
              if (positiveFile(rep[r])) {
                res.push(shortFile(rep[r]));
              }
            }
          }
        }
        var u = content.osxcollector_result[j].url;
        if (u && u.indexOf("http") === 0) {
          var rep = executeCommand('url', {url: u});
          if (rep && Array.isArray(rep)) {
            for (var r = 0; r < rep.length; r++) {
              if (positiveUrl(rep[r])) {
                res.push(shortUrl(rep[r]));
              }
            }
          }
        }
      }
    }
  }
}
if (res.length > 0) {
  return res;
}
return 'No infected files or malicious urls detected on OSX machine: '+args.system;
