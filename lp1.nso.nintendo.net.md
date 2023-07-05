Some quick documentation on getting the NSO webapplet in your browser (from information discovered by Samuel Elliot):
```
https://accounts.nintendo.com/connect/1.0.0/authorize?client_id=f4e5f2f3e022208b&response_type=id_token&scope=openid&redirect_uri=nintendo://lhub.nx.sys&state=a
```
Get id_token from the above.

Go to <https://lp1.nso.nintendo.net> -- set your user agent to something like `Mozilla/5.0 (Nintendo Switch; NsoApplet; Nintendo Switch) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.22.5 NintendoBrowser/5.1.0.23519`

Add breakpoints to the index's script at `var n = navigator.userAgent.includes("NintendoBrowser");` and the static/js/main.1d72eb58.js at `setNaAuthTokenAvailableCallback: function(e) {e(void 0, void 0, EP.b)},`

Reload page and, on first breakpoint, paste the below
```
Object.defineProperty(navigator, 'userAgent', {get: () => 'no'})
```
Then resume and on second breakpoint, paste the below, replacing "id_token" with your id_token from before
```
e(undefined, undefined, 'id_token')
```
