var app = angular.module('Home',[]);

app.controller('HomeController', function($scope, $window, $http, $sce) {
    $scope.tabTitle = $sce.trustAsHtml("Resum\u00E9");
});