angular.module('carpool').controller("NavbarController", function($location, $scope) {

    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
});