/**
 *
 Copyright (C) 2013  FreedomSponsors

 The JavaScript code in this page is free software: you can
 redistribute it and/or modify it under the terms of the GNU
 AFFERO GENERAL PUBLIC LICENSE (GNU AGPL) as published by the Free Software
 Foundation, either version 3 of the License, or (at your option)
 any later version.  The code is distributed WITHOUT ANY WARRANTY;
 without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the GNU GPL for more details.

 As additional permission under GNU GPL version 3 section 7, you
 may distribute non-source (e.g., minimized or compacted) forms of
 that code without the copy of the GNU GPL normally required by
 section 4, provided you include this license notice and a URL
 through which recipients can access the Corresponding Source.

 For more information, refer to
 https://github.com/freedomsponsors/www.freedomsponsors.org/blob/master/AGPL_license.txt
 */


var mod = angular.module('tagapi', []);

mod.factory('TagApi', function($http) {
    var add_tag = '/core/json/add_tag';
    var remove_tag = '/core/json/remove_tag';

    function addTag(name, objtype, objid){
        return $http({
            method: 'POST',
            url: add_tag,
            data: $.param({
                name: name,
                objtype: objtype,
                objid: objid
            })
        })
    }
    function removeTag(name, objtype, objid){
        return $http({
            method: 'POST',
            url: remove_tag,
            data: $.param({
                name: name,
                objtype: objtype,
                objid: objid
            })
        })
    }

    return {
        addTag: addTag,
        removeTag: removeTag
    }
});
