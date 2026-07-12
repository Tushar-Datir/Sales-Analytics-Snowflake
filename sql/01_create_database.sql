-- ==========================================
-- Create Warehouse
-- ==========================================

CREATE WAREHOUSE IF NOT EXISTS SALES_WH
WITH
WAREHOUSE_SIZE='XSMALL'
AUTO_SUSPEND=60
AUTO_RESUME=TRUE;

-- ==========================================
-- Create Database
-- ==========================================

CREATE DATABASE IF NOT EXISTS SALES_ANALYTICS_DB;