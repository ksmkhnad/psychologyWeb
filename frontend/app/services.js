app.factory('DataService', ['$http', function($http) {
    var apiBaseUrl = 'http://localhost/api'; // Ensure this is correct

    return {
        addStudentDiagnostics: function(data) {
            return $http.post(apiBaseUrl + '/diagnostics/students', data);
        },
        addTeacherDiagnostics: function(data) {
            return $http.post(apiBaseUrl + '/diagnostics/teachers', data);
        },
        addParentDiagnostics: function(data) {
            return $http.post(apiBaseUrl + '/diagnostics/parents', data);
        }
    };
}]);