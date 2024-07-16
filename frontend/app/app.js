var app = angular.module('psychServiceApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'app/views/index.html',
            controller: 'MainCtrl'
        })
        .when('/report', {
            templateUrl: 'app/views/report.html',
            controller: 'ReportCtrl'
        })
        .otherwise({
            redirectTo: '/'
        });
}]);