angular.module('carpool').controller("NewTripController", function($location, $http, $scope) {

    $scope.submit = function() {
        console.log($scope.newtrip);
        $http.post('/newtrip', angular.toJson($scope.newtrip) )
             .success(function(){ $location.path('/index') })
             .error(function(){alert('fail')});
    };

        $scope.master = {};
    $scope.reset = function() {
        $scope.newtrip = angular.copy($scope.master);
    };
});