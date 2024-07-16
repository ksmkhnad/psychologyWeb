app.factory('DataService', ['$http', function($http) {
    var baseUrl = 'http://localhost:5000/api/data';

    return {
        getData: function() {
            return $http.get(baseUrl);
        },
        addData: function(data) {
            return $http.post(baseUrl, data);
        }
    };
}]);
