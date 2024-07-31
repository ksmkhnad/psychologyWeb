var app = angular.module('psychServiceApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl : 'app/views/index.html'
    })
    .when('/report', {
        templateUrl : 'app/views/report.html'
    })
    .when('/diagnostics', {
        templateUrl : 'app/views/diagnostics.html',
        controller: 'DiagnosticsCtrl'
    })
    .otherwise({
        redirectTo: '/'
    });
}]);
