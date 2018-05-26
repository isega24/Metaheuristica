define(["require","exports","tslib","external/classnames","external/react","modules/clean/em_string","modules/clean/previews/util","modules/clean/react/file_viewer/file_utils","modules/clean/react/starred/star","modules/clean/react/starred/constants","modules/clean/react/title_bubble","modules/clean/react/home/resource_id_types","modules/clean/react/starred/actions","modules/core/i18n","modules/clean/react/size_class/constants"],function(e,t,r,i,n,s,o,a,l,u,d,c,m,p,f){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var h=(function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.hasFetchedStarStatus=!1,t.shouldDisplayStarred=function(){var e=t.props,r=e.sizeClass,i=e.sharedLinkInfo;return e.shouldDisplayStarred&&r===f.SizeClass.Large&&!i},t}return r.__extends(t,e),t.prototype.componentWillMount=function(){this.fetchStarred()},t.prototype.componentWillReceiveProps=function(){this.fetchStarred()},t.prototype.fetchStarred=function(){var e=this;this.shouldDisplayStarred()&&!this.hasFetchedStarStatus&&(this.hasFetchedStarStatus=!0,setTimeout(function(){e.props.user&&e.props.file.file_id&&m.StarredActions.fetchStatuses(e.props.user.role,[{id:e.props.file.file_id,type:c.HOME_RESOURCE_ID_TYPE.ENCODED_FILE_OBJ_ID}])},0))},t.prototype.render=function(){var e=this.props,t=e.file,r=e.maxFilenameEmLength,o=e.sharedLinkInfo,m=e.shouldDisplayMetadata,p=e.sizeClass,h=e.user,S=p===f.SizeClass.Large,y=S&&!!o&&!!o.ownerTeamName,T=S&&!o&&!!t.ts,g=i({fileinfo:!0,"u-pad-top-xxs":y||T,"u-pad-right-xs":!0});return n.createElement("div",{className:g},n.createElement("h1",{className:"filename"},n.createElement("div",{className:"filename--text"},s.Emstring.em_snippet(a.getFilename(t),r)),this.shouldDisplayStarred()?n.createElement(l.Star,{id:t.file_id,idType:c.HOME_RESOURCE_ID_TYPE.ENCODED_FILE_OBJ_ID,ref:"Star",user:h,tooltipPosition:d.TitleBubble.POSITIONS.BOTTOM,source:u.StarredSource.FILE_VIEWER}):null),m&&y?n.createElement(_,{sharedLinkInfo:o}):null,m&&T?n.createElement(E,{file:t,user:h}):null)},t.defaultProps={shouldDisplayStarred:!0,shouldDisplayMetadata:!0},t})(n.Component);t.Title=h;var _=(function(e){function t(){return null!==e&&e.apply(this,arguments)||this}return r.__extends(t,e),Object.defineProperty(t.prototype,"ownerText",{get:function(){var e=this.props.sharedLinkInfo,t=e.ownerName,r=e.ownerTeamName;return t?p._("from %(owner)s (%(team)s)").format({owner:s.Emstring.em_snippet(t,24),team:s.Emstring.em_snippet(r,18)}):p._("from %(team)s").format({team:s.Emstring.em_snippet(r,18)})},enumerable:!0,configurable:!0}),t.prototype.render=function(){return n.createElement("span",{className:"file-modifier"},this.ownerText)},t})(n.Component),E=(function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.getModifierString=function(){var e=t.props.file,r=e.last_modified_name;return 2!==e.event_type?p._("Modified ",{comment:"Like 'Modified just now"}):r?p._("%(modifier)s edited ",{comment:"Like 'John Smith edited just now'"}).format({modifier:r}):p._("You edited ",{comment:"Like 'You edited just now'"})},t.redirectToVersionHistory=function(){var e=t.props,r=e.file,i=e.user;if(!i)throw new Error("no user set");o.redirectToVersionHistory(r,i)},t}return r.__extends(t,e),t.prototype.render=function(){var e=this.props.file;return n.createElement("span",{className:"file-modifier"},this.getModifierString(),n.createElement(d.TitleBubble,{content:p._("View version history"),position:d.TitleBubble.POSITIONS.BOTTOM,isTargetPositionFixed:!0},n.createElement("a",{className:"file-modifier",onClick:this.redirectToVersionHistory,href:"#"},o.getModifierString(e))))},t})(n.Component)});
//# sourceMappingURL=title.min.js-vflhKyqCx.map