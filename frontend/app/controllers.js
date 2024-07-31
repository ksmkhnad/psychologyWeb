app.controller('DiagnosticsCtrl', ['$scope', 'DataService', function($scope, DataService) {
    $scope.studentData = {};
    $scope.teacherData = {};
    $scope.parentData = {};

    $scope.submitStudentDiagnostics = function() {
        DataService.addStudentDiagnostics($scope.studentData).then(function(response) {
            $scope.studentData = {}; // Clear the form
        });
    };

    $scope.submitTeacherDiagnostics = function() {
        DataService.addTeacherDiagnostics($scope.teacherData).then(function(response) {
            $scope.teacherData = {}; // Clear the form
        });
    };

    $scope.submitParentDiagnostics = function() {
        DataService.addParentDiagnostics($scope.parentData).then(function(response) {
            $scope.parentData = {}; // Clear the form
        });
    };
}]);