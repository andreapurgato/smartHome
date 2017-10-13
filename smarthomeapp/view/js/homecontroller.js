/**
 * Created by Andrea on 13/10/2017.
 */

// application variable
var smartHomeApp = angular.module('smartHomeApp', []);

/**
 * Controller for DIV.
 */
smartHomeApp.controller('MyCtrl', function MyCtrl($scope) {
    $scope.visible = true;

    $scope.toggle = function() {
        $scope.visible = !$scope.visible;
    };
});
