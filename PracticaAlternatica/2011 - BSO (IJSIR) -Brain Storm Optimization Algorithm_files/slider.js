define(["require","exports","external/classnames","external/create-react-class","external/react","external/react-dom-factories","external/prop-types","external/react-addons-pure-render-mixin","modules/clean/css"],function(e,r,i,s,n,t,a,c,o){"use strict";function d(e,r,i){for(var s=[],n=e<r,t=i?n?r+1:r-1:r,a=e;n?a<t:a>t;n?a++:a--)s.push(a);return s}Object.defineProperty(r,"__esModule",{value:!0});var l=s({displayName:"IndicatorGroup",mixins:[c],propTypes:{className:a.string,currentSlideIndex:a.number.isRequired,slideCount:a.number.isRequired,onIndicatorClick:a.func},render:function(){var e=this;return t.ul({className:i("c-slider__indicator-group",this.props.className)},d(0,this.props.slideCount,!1).map(function(r){return t.li({key:"indicator-"+r,className:i({"c-slider__indicator":!0,"is-active":r===e.props.currentSlideIndex}),onClick:function(){return"function"==typeof e.props.onIndicatorClick?e.props.onIndicatorClick(r):void 0}})}))}});r.IndicatorGroup=l;var p=s({displayName:"NavButtonGroup",mixins:[c],propTypes:{className:a.string},render:function(){return t.div({className:i("c-slider__nav-button-group",this.props.className)},this.props.children)}});r.NavButtonGroup=p;var u=s({displayName:"Slides",mixins:[c],propTypes:{currentSlideIndex:a.number.isRequired,width:a.number.isRequired,height:a.number},getSlideCount:function(){return n.Children.count(this.props.children)},render:function(){var e=this;return t.div({className:"c-slider__window",style:{width:this.props.width+"px",height:null!=this.props.height?this.props.height:"auto"}},t.div({className:"c-slider__slides"},n.Children.map(this.props.children,function(r,s){return t.div({className:i({"c-slider__slide":"c-slider__slide","is-active":e.props.currentSlideIndex===s}),style:{width:e.props.width+"px",transform:"translateX("+100*-e.props.currentSlideIndex+"%)"}},r)})))}});r.Slides=u;var m=s({displayName:"Slider",mixins:[c],propTypes:{className:a.string},componentWillMount:function(){return o.require_css("/static/css/legacy_packages/components-vflj18kpx.css")},render:function(){return t.div({className:i("c-slider",this.props.className)},this.props.children)}});r.Slider=m});
//# sourceMappingURL=slider.min.js-vflHrbJ5R.map