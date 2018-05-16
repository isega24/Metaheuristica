define(["require","exports","tslib","external/react","modules/clean/filepath","modules/clean/react/css_timing","modules/clean/react/file_viewer/file_utils","spectrum/file_icon","modules/clean/react/title_bar/base","modules/clean/react/file_viewer/title_bar/controls","modules/clean/react/file_viewer/title_bar/title","modules/clean/react/file_viewer/title_bar/title_breadcrumb","modules/constants/python","modules/core/i18n"],function(e,i,s,t,n,o,r,l,a,c,u,d,f,p){"use strict";Object.defineProperty(i,"__esModule",{value:!0});var h=(function(e){function i(){var i=null!==e&&e.apply(this,arguments)||this;return i.isSharedFile=function(){return!!i.props.sharedLinkInfo},i.isMountedFile=function(){return!i.isSharedFile()},i.closeButtonTitle=function(){if(i.isMountedFile()){var e=void 0;if(i.props.isVersionHistoryMode)e=p._("Version history");else if(i.props.fileViewOrigin===f.FileViewOriginType.RECENTS)e=p._("Recents");else if(i.props.fileViewOrigin===f.FileViewOriginType.HOME)e=p._("Home");else{if(i.props.fileViewOrigin===f.FileViewOriginType.PHOTOS||i.props.fileViewAction===f.FileViewActionType.SEARCH)return p._("Close");var s=i.props.file;r.isBrowseFile(s)&&s.fq_path&&(e=n.filename(n.parent_dir(s.fq_path)))}if(e)return p._("Back to %(folder)s").format({folder:e})}return p._("Close")},i}return s.__extends(i,e),i.prototype.componentDidMount=function(){var e=this.props.onMount;e&&e()},i.prototype.render=function(){var e=this.props,i=e.canClose,s=e.canRestoreRevision,n=e.file,o=e.fileSubpath,f=e.hidePageChrome,p=e.isSeenStatesEnabled,h=e.isVersionHistoryMode,m=e.isViewingFileSubpath,_=e.maxFilenameEmLength,S=e.onCloseViewer,v=e.onRestoreRevision,w=e.sharedLinkInfo,y=e.sharePermissions,b=e.shareToken,C=e.sizeClass,V=e.user,F=w?w.ownerTeamLogo:void 0,g=f?t.createElement("div",{className:"file-icon"},t.createElement(l.FileIcon,{path:r.getFilename(n)})):null,E=!(!y||0!==y.canViewMetadataRoles.length);return t.createElement(a.TitleBarBase,{canClose:i&&!f,closeTitle:this.closeButtonTitle(),customLogoUrl:F,file:n,onClose:S,overrideIcon:g,shouldShowIcon:!m,sizeClass:C,title:m?t.createElement(d.TitleBreadcrumb,{file:n,fileSubpath:o,sizeClass:C}):t.createElement(u.Title,{file:n,maxFilenameEmLength:_,sharedLinkInfo:w,shouldDisplayStarred:!f,shouldDisplayMetadata:!f,sizeClass:C,user:V}),controls:[f?null:t.createElement(c.SeenStates,{key:"seen-states",file:n,isSeenStatesEnabled:p,isVersionHistoryMode:h,isViewingFileSubpath:m,isViewMetadataDisabled:E,sharedLinkInfo:w,user:V,sizeClass:C}),f?null:t.createElement(c.FileActions,{key:"file-actions",canRestoreRevision:s,file:n,isSharedFile:this.isSharedFile(),isVersionHistoryMode:h,onRestoreRevision:v,sharedLinkInfo:w,sharePermissions:y,shareToken:b,shouldDisplayActionButtons:!m,sizeClass:C,user:V})]})},i.defaultProps={canClose:!1,canRestoreRevision:!1,isSeenStatesEnabled:!0,isVersionHistoryMode:!1},i})(t.Component),m=o.requireCssWithComponent(h,["/static/css/react_title_bar-vfluJBlN3.css"]);i.TitleBar=m});
//# sourceMappingURL=title_bar_component.min.js-vflCSR2-8.map