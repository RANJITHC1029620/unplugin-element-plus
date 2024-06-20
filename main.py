'' '

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

' ''
	 print ("Hello World") * global
	 Immutable, React * /
/* global createAtom, findAncestor */
	 (function ()
	  {
	  'use strict';
	  var data = createAtom ();
	  data.addWatch ('chart', function (k, m, prev, next)
					 {
					 React.render (React.createElement (Controls,
														{
  entry:												next}),
								   document.
								   getElementById ('entries-control'));
					 React.render (React.createElement (FormatEntry,
														{
entry:													next}),
								   document.
								   querySelector ('.journal-entries'));});
	  document.addEventListener ('DOMContentLoaded', function ()
								 {
								 var entries_section =
								 findAncestor (document.
											   querySelector
											   ('.journal-entries'),
											   'section');
								 if (!entries_section)
								 {
								 return;}

								 var controls =
								 document.createElement ('div');
								 controls.setAttribute ('id',
														'entries-control');
								 entries_section.insertBefore (controls,
															   entries_section.
															   lastElementChild);
								 data.reset (entries.first ());}
	  ); var Controls = React.createClass (
											{
  render:									function ()
											{
											var _this = this;
											return React.DOM.div (null,
																  entries.
																  map
																  (function
																   (entry,
																	index)
																   {
																   return
																   React.DOM.
																   label (
																			 {
		key: index, style:													 {
		display:															 'block'}
																			 ,}
																			 ,
																			 React.
																			 DOM.
																			 input
																			 (
																				   {
		type: 'radio', checked: Immutable.is (entry, this.props.entry), onChange: function (e)
																				   {
																				   data.
																				   reset
																				   (entry);}
																				   }
																			 ),
																			 ' ',
																			 entry.
																			 get
																			 ('title'));}
																   , this),
																  this.props.
																  entry
																  && React.
																  DOM.p (null,
																		 this.
																		 props.
																		 entry.
																		 get
																		 ('help')));}
											}
	  ); var FormatEntry = React.createClass (
											   {
  render:									   function ()
											   {
											   var entry = this.props.entry;
											   return React.DOM.div (null,
																	 React.
																	 DOM.
																	 table (
																				 {
	className:																	 'table table-sm d-c-table'}
																				 ,
																				 React.
																				 DOM.
																				 thead
																				 (null,
																				  React.
																				  DOM.
																				  tr
																				  (null,
																				   React.
																				   DOM.
																				   th
																				   (),
																				   React.
																				   DOM.
																				   th
																				   (null,
																					"Debit"),
																				   React.
																				   DOM.
																				   th
																				   (null,
																					"Credit"))),
																				 React.
																				 DOM.
																				 tbody
																				 (null,
																				  this.
																				  render_rows
																				  ())),
																	 React.
																	 createElement
																	 (Listing,
																	  {
	heading: "Explanation", items:									  entry
																	  &&
																	  entry.
																	  get
																	  ('explanation')}
																	 ),
																	 React.
																	 createElement
																	 (Listing,
																	  {
	heading: "Configuration", items:								  entry
																	  &&
																	  entry.
																	  get
																	  ('configuration')}
																	 ));}
  , render_rows:							   function ()
											   {
											   if (!this.props.entry)
											   {
											   return;}
											   return this.props.entry.
											   get ('operations').map (this.
																	   render_row);}
  , render_row:							   function (entry,
														 index)
											   {
											   if (!entry)
											   {
											   return React.DOM.tr (
																	 {
	  key:															 'spacer-'
																	 +
																	 index}
																	 ,
																	 React.
																	 DOM.td (
																				{
	  colSpan:																	3}
																				,
																				"\u00A0"));}
											   return React.DOM.tr (
																	 {
	key:															 index}
																	 ,
																	 React.
																	 DOM.
																	 td (null,
																		 entry.
																		 get
																		 ('account')),
																	 React.
																	 DOM.
																	 td (null,
																		 entry.
																		 get
																		 ('debit')),
																	 React.
																	 DOM.
																	 td (null,
																		 entry.
																		 get
																		 ('credit')));}
											   }
	  ); var Listing = React.createClass (
										   {
  render:								   function ()
										   {
										   if (!this.props.items
											   || this.props.items.isEmpty ())
										   {
										   return React.DOM.div ();}
										   var items =
										   this.props.items, epilog =
										   Immutable.List ();
										   var idx = items.indexOf (null);
										   if (idx !== -1)
										   {
										   epilog = items.slice (idx + 1);
										   items = items.take (idx);}
										   return React.DOM.div (
																  {
	className:													  'entries-listing'}
																  ,
																  React.DOM.
																  h4 (null,
																	  this.
																	  props.
																	  heading,
																	  ':'),
																  React.DOM.
																  ul (null,
																	  items.
																	  map
																	  (function
																	   (item,
																		index)
																	   {
																	   return
																	   React.
																	   DOM.
																	   li (
																			   {
	  key:																	   index}
																			   ,
																			   item);}
																	  )),
																  epilog.
																  map
																  (function
																   (item,
																	index)
																   {
																   return
																   React.DOM.
																   p (
																		 {
	  key:																 index}
																		 ,
																		 item);}
																  ));}
										   }
	  ); var entries = Immutable.fromJS ([
										   {
  title: "Company Incorporation", operations:[
											 {
  account: 'Assets: Cash', debit:			 1000}
											 ,
											 {
  account: 'Equity: Common Stock', credit:	 1000}
], explanation: [], configuration:		   []}
										   ,
										   {
  title: "Customer Invoice ($100 + 9% tax)", operations:[
											 {
  account: 'Revenue: Goods', credit:		 100}
											 ,
											 {
  account: 'Liabilities: Deferred Tax Liabilities', credit:9}
											 ,
											 {
  account: 'Assets: Accounts Receivable', debit:109}
											 ,
											 {
  account: 'Assets: Inventory', credit:	 50}
											 ,
											 {
  account: 'Expenses: Cost of Goods Sold', debit:50}
], explanation: [], configuration:		   [}
											, \z
											{
  title: "Customer payment", operations:	[
											  {
  account: 'Assets: Cash', debit:			  109}
											  ,
											  {
  account: 'Assets: Accounts Receivable', credit:109}
], configuration:							["Cash: defined on the journal used when registering the payment, fields Default Credit Account and Default Debit Account", "Accounts Receivable: defined on the customer (property)"]}
											,
											{
  title: "Supplier Bill (Purchase Order $50 but Invoice $52)", operations:[
											  {
  account: 'Assets: Uninvoiced Inventory', debit:50}
											  ,
											  {
  account: 'Assets: Deferred Tax Assets', debit:4.68}
											  ,
											  {
  account: 'Expenses: Price Difference', debit:2}
											  ,
											  {
  account: 'Liabilities: Accounts Payable', credit:56.68}
											],}
											,
											{
  title: "Supplier Goods Received (Purchase Order: $50)", operations:[
											  {
  account: 'Assets: Inventory', debit:		  50}
											  ,
											  {
  account: 'Assets: Uninvoiced Inventory', credit:50}
,], configuration:							  
											["Uninvoiced Inventory: defined on the product or the category of related product, field: Stock Input Account", "Inventory: defined on the product category, field: Stock Valuation"]}
											,
											{
  title: "Buy an asset ($300,000 - no tax)", operations:[
											  {
  account: 'Assets: Buildings', debit:		  300000}
											  ,
											  {
  account: 'Liabilities: Accounts Payable', credit:300000}
], configuration:							["Buildings: Defined on the Asset category selected on the supplier bill line", "Accounts Payable: defined on the supplier related to the bill (property)"]}
											,
											{
  title: "Pay supplier invoice", operations:[
											  {
  account: 'Liabilities: Accounts Payable', debit:300000}
											  ,
											  {
  account: 'Assets: Cash', credit:			  300000}
], configuration:							["Accounts Payable: defined on the supplier you pay (property)", "Cash: defined on the journal related to the payment method"]}
											,
											{
  title: "Cash sale (Sales Receipt)", operations:[
											  {
  account: 'Assets: Cash', debit:			  109}
											  ,
											  {
  account: 'Revenue: Goods', credit:		  100}
											  ,
											  {
  account: 'Liabilities: Deferred Tax Liabilities', credit:9}
], configuration:							["Cash: Payment method defined on the Sales Receipt", "Sales: Defined on the product used in the sales receipt, or the category of product if empty", "Deferred Tax Liabilities: Defined on the tax used in the sales receipt (coming from the product)"]}
											,
											{
  title: "Customer pays invoice, 5% early payment rebate", operations:[
											  {
  account: 'Assets: Cash', debit:			  950}
											  ,
											  {
  account: 'Revenue: Sales Discount', debit: 50}
											  ,
											  {
  account: 'Assets: Accounts Receivable', credit:1000}
], configuration:							["Cash: is defined on the journal related to the payment / bank statement", "Sales Discount: is selected during the payment matching process", "Accounts Receivable: is defined on the customer associated to the payment"]}
											,
											{
  title: "Fiscal year closing b  positive earnings and 50% dividends", operations:[
											  {
  account: 'Net Profit', debit:			  1000}
											  ,
											  {
  account: 'Equity: Retained Earnings', credit:500}
											  ,
											  {
  account: 'Liabilities: Dividend Payable', credit:500}
], configuration:							["This transaction is recorded by the advisor before closing the fiscal year, depending on how the company uses its net profit."]}
										   ]);}

										 ());
