app.controller('MainCtrl', ['$scope', 'DataService', function($scope, DataService) {
    $scope.formData = {};

    $scope.submitForm = function() {
        DataService.addData($scope.formData).then(function(response) {
            $scope.formData = {}; // Clear the form
        });
    };
}]);

app.controller('ReportCtrl', ['$scope', 'DataService', function($scope, DataService) {
    DataService.getData().then(function(response) {
        $scope.data = response.data;
    });
}]);
