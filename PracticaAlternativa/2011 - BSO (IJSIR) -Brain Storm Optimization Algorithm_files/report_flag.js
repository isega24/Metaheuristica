define(["require","exports","tslib","external/react","modules/clean/react/title_bubble","modules/clean/react/css","modules/clean/react/overlay","modules/core/i18n","modules/core/uri"],function(e,t,r,s,o,i,n,a,l){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var u=(function(e){function t(){return null!==e&&e.apply(this,arguments)||this}return r.__extends(t,e),t.prototype.getHref=function(){var e={ssu:this.props.sharedLink};return this.props.isFolderLink&&(e.isFolderLink=JSON.stringify(this.props.isFolderLink),e.shareToken=JSON.stringify(this.props.shareToken)),new l.URI({scheme:"https",authority:"www.dropbox.com",path:"/report_abuse",query:e}).toString()},t.prototype.render=function(){var e=n.PositionedOverlay.POSITIONS.RIGHT;return o.TitleBubble.POSITIONS&&(e=o.TitleBubble.POSITIONS.RIGHT),s.createElement(o.TitleBubble,{content:a._("Report an issue"),position:e,distanceFromTarget:5,isTargetPositionFixed:!0},s.createElement("div",{className:"report-flag"},s.createElement("a",{href:this.getHref(),rel:"noopener noreferrer",className:"flag-link",target:"_blank",title:a._("Report as issue")}," ")))},t})(s.Component),c=i(u,["/static/css/abuse/report_flag-vflt1ytDn.css"]);t.ReportFlag=c});
//# sourceMappingURL=report_flag.min.js-vflLOFLbd.map