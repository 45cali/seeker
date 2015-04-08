"use strict";var app=angular.module("seekerUiApp",["ngAnimate","ngCookies","ngResource","ngRoute","ngSanitize","ngTouch","angular-jwt","ngStorage","smart-table","ui.sortable"]).config(["$routeProvider",function(a){a.when("/",{templateUrl:"views/main.html",controller:"MainCtrl"}).when("/about",{templateUrl:"views/about.html",controller:"AboutCtrl"}).when("/api",{templateUrl:"views/api.html",controller:"ApiCtrl"}).when("/sops",{templateUrl:"views/sops.html",controller:"SopsCtrl"}).when("/sops/:sopId",{templateUrl:"views/thissop.html",controller:"ThisSopCtrl"}).when("/sops/edit/:sopId",{templateUrl:"views/editthissop.html",controller:"EditThisSopCtrl"}).when("/create/sops",{templateUrl:"views/createsop.html",controller:"CreateSopCtrl"}).when("/templates",{templateUrl:"views/templates.html",controller:"TemplatesCtrl"}).when("/templates/:templateId",{templateUrl:"views/thistemplate.html",controller:"ThisTemplateCtrl"}).when("/templates/edit/:templateId",{templateUrl:"views/editthistemplate.html",controller:"EditThisTemplateCtrl"}).when("/create/templates",{templateUrl:"views/createtemplate.html",controller:"CreateTemplateCtrl"}).otherwise({redirectTo:"/"})}]);angular.module("seekerUiApp").controller("MainCtrl",["$scope","seeker","backendHost",function(a,b,c){console.log(c.backendPath()),a.getRequestSeeker=function(c,d){var e=b.lookup(c,d);e.then(function(b){var c=b.data.data_passed.results;"string"==typeof c?(a.noMatch=!0,a.matchFound=!1):c instanceof Array&&(a.noMatch=!1,a.matchFound=!0,a.searchResult=c)})}}]),angular.module("seekerUiApp").controller("AboutCtrl",["$scope",function(a){a.awesomeThings=["HTML5 Boilerplate","AngularJS","Karma"]}]),angular.module("seekerUiApp").controller("ApiCtrl",["$scope",function(a){a.awesomeThings=["HTML5 Boilerplate","AngularJS","Karma"]}]),angular.module("seekerUiApp").controller("SopsCtrl",["$scope","checkJwt","sop","$location",function(a,b,c,d){b.validate(),c.list().success(function(){}).error(function(){}).then(function(b){console.log("then"+b),a.sopCollection=b.data}),angular.element(".focusHere").focus(),a.goToThisSop=function(a){d.path("/sops/"+a)},a.goToCreateSop=function(){d.path("create/sops/")}}]),angular.module("seekerUiApp").factory("seeker",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/seek/?";return{lookup:function(b,c){return a.get(angular.isUndefined(c)||""===c?d+"hostname="+b:d+"hostname="+b+"&alert="+c)}}}]),angular.module("seekerUiApp").controller("MyloginCtrl",["$scope","$http","$localStorage","$route","backendHost",function(a,b,c,d,e){a.login=function(a,f){var g=e.backendPath(),h=g.baseUrl+"/api-token-auth/",i={method:"POST",url:h,headers:{"Content-Type":"application/json"},data:{username:a,password:f}};b(i).success(function(a){c.token=a.token,$("#loginLink").hide(),$("#loggedIn").show(),$("#headerSop").show(),$("#headerTemplate").show()}).error(function(){}).then(function(){d.reload()})}}]),angular.module("seekerUiApp").controller("HeaderCtrl",["$scope","$localStorage","jwtHelper","checkJwt",function(a,b,c,d){if($("#loginLink").show(),$("#loggedIn").hide(),$("#headerSop").hide(),$("#headerTemplate").hide(),"undefined"==typeof b.token);else{a.$storage=b;var e=a.$storage.token,f=c.isTokenExpired(e);if(f===!1){var g=c.decodeToken(e);a.currentUser=g.username,$("#loginLink").hide(),$("#loggedIn").show(),$("#headerSop").show(),$("#headerTemplate").show()}else delete a.$storage.token}a.logout=function(){delete a.$storage.token,d.validate()}}]),angular.module("seekerUiApp").controller("TemplatesCtrl",["$scope","checkJwt","template","$location",function(a,b,c,d){b.validate(),c.list().success(function(){}).error(function(){}).then(function(b){a.templateCollection=b.data}),angular.element(".focusHere").focus(),a.goToThisTemplate=function(a){d.path("/templates/"+a)},a.goToCreateTemplate=function(){d.path("create/templates/")}}]),angular.module("seekerUiApp").factory("template",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/templates/";return{list:function(){return a.get(d)},get:function(b){return a.get(d+b)},put:function(b,c,d,e,f){return a({method:"PUT",url:b,headers:{"Content-Type":"application/json",Authorization:"JWT "+f},data:{name:c,description:d,alert_set:e,owner:"me"}})},post:function(b,c,e,f){return a({method:"POST",url:d,headers:{"Content-Type":"application/json",Authorization:"JWT "+f},data:{name:b,description:c,alert_set:e,owner:"me"}})},"delete":function(b,c){return a({method:"DELETE",url:b,headers:{"Content-Type":"application/json",Authorization:"JWT "+c}})}}}]),angular.module("seekerUiApp").service("checkJwt",["$localStorage","$location","jwtHelper",function(a,b,c){this.validate=function(){"undefined"!=typeof a.token?c.isTokenExpired(a.token)===!0&&(delete a.token,$("#loginLink").show(),$("#loggedIn").hide(),$("#headerSop").hide(),$("#headerTemplate").hide(),b.path("/")):($("#loginLink").show(),$("#loggedIn").hide(),$("#headerSop").hide(),$("#headerTemplate").hide(),b.path("/"))}}]),angular.module("seekerUiApp").directive("autoFocus",["$timeout",function(a){return{restrict:"AC",link:function(b,c){a(function(){c[0].focus()},0)}}}]),angular.module("seekerUiApp").controller("ThisTemplateCtrl",["$scope","$routeParams","template","checkJwt","checkPerm","$location",function(a,b,c,d,e,f){d.validate();var g=b.templateId;c.get(g).success().error().then(function(b){a.thisTemplate=b.data,a.isOwner=e.isOwner(b.data.owner)}),a.editTemplate=function(a){f.url("/templates/edit/"+a)},a.goBack=function(){f.url("/templates/")}}]),angular.module("seekerUiApp").controller("EditThisTemplateCtrl",["$scope","checkJwt","checkPerm","template","$routeParams","alerts","$localStorage","$location",function(a,b,c,d,e,f,g,h){b.validate(),a.showUpdate=!1;var i=e.templateId;d.get(i).success(function(){}).error(function(){}).then(function(b){c.isOwnerOrRedirect(b.data.owner),a.editThisTemplate=b.data,a.templateList=a.editThisTemplate.alert_set,a.thisTextArea=a.editThisTemplate.description}).then(function(){f.get().success(function(){}).error(function(){}).then(function(b){a.masterList=f.listify(b.data)})}),a.addAlertToTemplateList=function(b){a.templateList.indexOf(b)>-1||"undefined"==typeof b?a.thisAlert="":"undefined"!=typeof b&&b.length>0&&(a.templateList.push(b),a.thisAlert="")},a.removeFromTemplateList=function(b,c){console.log(a.templateList[b]),a.templateList.splice(a.templateList.indexOf(c),1),console.log(a.templateList)},a.updateTemplate=function(){var b=a.editThisTemplate.url;console.log("url: "+b);var c=a.templateName;c="undefined"==typeof c?a.editThisTemplate.name:c.length<1?a.editThisTemplate.name:c,console.log("name: "+name);var e=a.thisTextArea;console.log("descriptiopn: "+e);var f=a.templateList;console.log("alert_set: "+typeof f+" val:"+f),console.log("token :"+g.token),d.put(b,c,e,f,g.token).success(function(){a.updateInfo="The update was a success",a.updateClass="alert alert-success"}).error(function(){a.updateInfo="There was an error and this information was not updated. If this issue continues, please contact the admin for this tool.",a.updateClass="alert alert-success"}).then(function(){a.showUpdate=!0})},a.deleteTemplate=function(){var b=a.editThisTemplate.url;d["delete"](b,g.token).success(function(){h.url("/templates")}).error(function(){}).then(function(){})},a.goBack=function(){h.url("/templates/"+i)}}]),angular.module("seekerUiApp").service("checkPerm",["$localStorage","jwtHelper","$location","groupNames","$q",function(a,b,c,d,e){var f=a.token,g=b.decodeToken(f);this.isOwner=function(a){return"undefined"!=typeof f?a===g.username?!0:!1:void 0},this.isGroup=function(a){if("undefined"!=typeof f){var b=e.defer();return d.get().then(function(c){var d=!1;c.indexOf(a)>=0&&(d=!0),b.resolve(d)}),b.promise}return!1},this.isOwnerOrRedirect=function(a){"undefined"!=typeof f&&(a===g.username||c.path("/templates"))},this.isGroupOrRedirect=function(a,b){b.indexOf(a)>=0||c.path("/sops")}}]),angular.module("seekerUiApp").factory("alerts",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/alerts/";return{get:function(){return a.get(d)},listify:function(a){var b=[];for(var c in a)b.push(a[c].alert);return b}}}]),angular.module("seekerUiApp").directive("onenter",function(){return function(a,b,c){b.bind("keydown keypress",function(b){13===b.which&&(a.$apply(function(){a.$eval(c.onenter)}),b.preventDefault())})}}),angular.module("seekerUiApp").controller("CreateTemplateCtrl",["$scope","checkJwt","alerts","$location","$localStorage","template",function(a,b,c,d,e,f){b.validate(),a.templateList=[],a.showCreate=!1,a.moreResponseDetail=!1,a.toggleShow=function(){a.moreResponseDetail=!a.moreResponseDetail,console.log("mrd: "+a.moreResponseDetail)},c.get().success(function(){}).error(function(){}).then(function(b){a.masterList=c.listify(b.data)}),a.addAlertToTemplateList=function(b){a.templateList.indexOf(b)>-1||"undefined"==typeof b?a.thisAlert="":"undefined"!=typeof b&&b.length>0&&(a.templateList.push(b),a.thisAlert="")},a.removeFromTemplateList=function(b,c){console.log(a.templateList[b]),a.templateList.splice(a.templateList.indexOf(c),1),console.log(a.templateList)},a.goBack=function(){d.url("/templates/")},a.createTemplate=function(){var b=a.templateName;console.log("description: "+b);var c=a.thisTextArea;console.log("description: "+c);var d=a.templateList;console.log("alert_set: "+typeof d+" val:"+d),console.log("token :"+e.token),f.post(b,c,d,e.token).success(function(c,d){a.createResponse={message:'Template "'+b+'" created',"class":"alert-success",status:d,data:c}}).error(function(b,c){a.createResponse={message:"There was an error creating this template","class":"alert-danger",status:c,data:b},a.showCreate=!0}).then(function(){a.showCreate=!0})}}]),angular.module("seekerUiApp").factory("sop",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/lookup/";return{list:function(){return a.get(d)},get:function(b){return a.get(d+b)},put:function(b,c,d,e,f,g,h,i,j){return a({method:"PUT",url:b,headers:{"Content-Type":"application/json",Authorization:"JWT "+c},data:{pattern:d,product:e,created_by:"me",owner:f,alert_set:g,info:h,oncall:i,email:j}})},post:function(b,c,e,f,g,h,i,j){return a({method:"POST",url:d,headers:{"Content-Type":"application/json",Authorization:"JWT "+b},data:{pattern:c,product:e,created_by:"me",owner:f,alert_set:g,info:h,oncall:i,email:j}})},"delete":function(b,c){return a({method:"DELETE",url:b,headers:{"Content-Type":"application/json",Authorization:"JWT "+c}})}}}]),angular.module("seekerUiApp").controller("ThisSopCtrl",["$scope","$location","sop","checkJwt","$routeParams","checkPerm",function(a,b,c,d,e,f){d.validate();var g=e.sopId;c.get(g).success(function(b){a.thisSop=b,f.isGroup(b.owner).then(function(b){a.isGroup=b})}).error().then(),a.goBack=function(){b.url("/sops")},a.editSop=function(a){b.url("/sops/edit/"+a)}}]),angular.module("seekerUiApp").factory("users",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/users/";return{list:function(){return a.get(d)}}}]),angular.module("seekerUiApp").factory("groups",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/groups/";return{list:function(){return a.get(d)},get:function(b){return a.get(d+b)}}}]),angular.module("seekerUiApp").service("groupNames",["groups","users","$localStorage","jwtHelper","$q",function(a,b,c,d,e){var f=c.token,g=d.decodeToken(f);this.get=function(){var c=e.defer();return b.list().then(function(b){a.list().then(function(a){var d=b.data,e=a.data,f=[],h=[];for(var i in d)if(d[i].username===g.username){f=d[i].groups;break}for(var j in f){var k=f[j];for(var l in e)e[l].id===k&&h.push(e[l].name)}c.resolve(h)})}),c.promise}}]),angular.module("seekerUiApp").controller("EditThisSopCtrl",["$scope","alerts","groupNames","sop","products","checkJwt","checkPerm","$routeParams","$location","template","jsonData","$localStorage",function(a,b,c,d,e,f,g,h,i,j,k,l){f.validate();var m=h.sopId,n=[];d.get(m).success(function(b){c.get().then(function(c){g.isGroupOrRedirect(b.owner,c),a.groupList=c}),a.sopGroup=b.owner,a.sopPattern=b.pattern,a.sopProduct=b.product,a.sopOncall=b.oncall,a.sopEmail=b.email,a.sopEscalationInfo=b.info,a.sopAlertSet=b.alert_set,n=b.alert_set,a.sopId=m,a.sopUrl=b.url}).then(function(){b.get().then(function(c){a.masterList=b.listify(c.data)}),e.list().then(function(b){a.productList=b.data}),j.list().then(function(b){a.templateList=b.data})}),a.addToAlertList=function(b){a.sopAlertSet.indexOf(b)>-1||"undefined"==typeof b?a.thisAlert="":"undefined"!=typeof b&&b.length>0&&(a.sopAlertSet.push(b),a.thisAlert="")},a.removeFromAlertList=function(b,c){a.sopAlertSet.splice(a.sopAlertSet.indexOf(c),1)},a.goBack=function(){i.url("/sops/"+m)},a.updateSopProduct=function(b){a.sopProduct=b},a.updateSopGroup=function(b){a.sopGroup=b},a.selectTemplate=function(b){a.sopTemplate=b.name,n=a.sopAlertSet,a.sopAlertSet=b.alert_set},a.previousAlertList=function(){a.sopAlertSet=n},a.deleteSop=function(){d["delete"](a.sopUrl,l.token).success(function(){i.url("/sops/")}).error(function(){}).then()},a.updateSop=function(){var b=a.sopUrl,c=l.token,e=a.sopPattern,f=a.sopProduct,g=a.sopGroup,h=a.sopAlertSet,i=a.sopEscalationInfo,j=a.sopOncall,k=a.sopEmail;d.put(b,c,e,f,g,h,i,j,k).success(function(){}).error(function(){}).then(function(){})},a.loadHelpInfo=function(){k.get("editsopinfo.json").then(function(b){a.sopEditHelpInfo=b.data})}}]),angular.module("seekerUiApp").factory("products",["$http","backendHost",function(a,b){var c=b.backendPath(),d=c.baseUrl+"/api/products/";return{list:function(){return a.get(d)}}}]),angular.module("seekerUiApp").factory("jsonData",["$location","$http",function(a,b){var c="data/";return{get:function(a){return console.log("jsonData path: "+c+a),b.get(c+a)}}}]),angular.module("seekerUiApp").controller("CreateSopCtrl",["$scope","checkJwt","groupNames","template","products","alerts","$location","$localStorage","sop","jsonData",function(a,b,c,d,e,f,g,h,i,j){b.validate(),a.sopAlertSet=[];var k=[];a.showCreateResponse=!1,a.showDetail=!1,c.get().then(function(b){a.groupList=b}),e.list().then(function(b){a.productList=b.data}),d.list().then(function(b){a.templateList=b.data}),a.selectTemplate=function(b){a.sopTemplate=b.name,k=a.sopAlertSet,a.sopAlertSet=b.alert_set},f.get().then(function(b){a.masterList=f.listify(b.data)}),a.goBack=function(){g.url("/sops")},a.previousAlertList=function(){a.sopAlertSet=k},a.addToAlertList=function(b){a.sopAlertSet.indexOf(b)>-1||"undefined"==typeof b?a.thisAlert="":"undefined"!=typeof b&&b.length>0&&(a.sopAlertSet.push(b),a.thisAlert="")},a.createSop=function(){var b=h.token,c=a.sopPattern,d=a.sopProduct,e=a.sopGroup,f=a.sopAlertSet,g=a.sopEscalationInfo,j=a.sopOncall,k=a.sopEmail;i.post(b,c,d,e,f,g,j,k).success(function(b){a.createStatus={message:"Sop created successfully",detail:b,"class":"alert-success"},a.showCreateResponse=!0}).error(function(b){a.createStatus={message:"There was an error in creating sop",detail:b,"class":"alert-danger"},a.showCreateResponse=!0})},a.removeFromAlertList=function(b,c){a.sopAlertSet.splice(a.sopAlertSet.indexOf(c),1)},a.updateSopProduct=function(b){a.sopProduct=b},a.updateSopGroup=function(b){a.sopGroup=b},a.showResponseDetail=function(){a.showDetail=!a.showDetail},a.loadHelpInfo=function(){j.get("editsopinfo.json").then(function(b){a.sopEditHelpInfo=b.data})}}]),angular.module("seekerUiApp").service("backendHost",["$location",function(a){var b={hostname:"localhost",port:"8000",baseUrl:"http://localhost:8000"},c={hostname:a.host(),port:a.port(),baseUrl:"http://"+a.host()+":"+a.port()};this.backendPath=function(){return console.log("localHost: "+a.host()),"localhost"===a.host()?(console.log("return dev"),b):(console.log("return prod"),c)}}]);